import click
from pathlib import Path

from src.kml_ilmnfqc.sample import get_sample_path_dict
from src.kml_ilmnfqc.fastqc import run_fastqc
from src.kml_ilmnfqc.multiqc import run_multiqc
from src.kml_ilmnfqc.fastp import run_fastp
from src.kml_ilmnfqc.stats import calc_fastp_stats


@click.command()
@click.option("--input-dir", required=True, type=click.Path(exists=True),
              help="输入 bcl2fastq 拆分后的 fastq 文件夹, 使用 '_S' 作为分隔符来确定样本名")
@click.option("--output-dir", default="ilmn-fqc-result", show_default=True, help="输出文件夹")
@click.option("--threads", default=8, type=int, show_default=True, help="线程数")
@click.option("--force", is_flag=True, help="强制重新运行")
@click.help_option(help="获取帮助信息")
def main(input_dir, output_dir, threads, force):
    """Illumina bcl2fastq 拆分后 fastq 快速质量评估流程"""
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    sample_path_dict = get_sample_path_dict(input_dir)
    run_fastqc(sample_path_dict, output_dir, threads, force)
    run_multiqc(output_dir, False)
    run_fastp(sample_path_dict, output_dir, threads, False)
    calc_fastp_stats(output_dir)
