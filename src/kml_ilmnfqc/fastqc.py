import logging
from pathlib import Path

from src.kml_ilmnfqc.config import ACTIVATE
from src.kml_ilmnfqc.util import get_thread_and_parallel_number, multi_run_command


def run_fastqc(fqpath_dict: dict, output_dir: Path, threads: int, force: bool) -> None:
    """
    运行 FastQC, 所有样本结果输入到一个目录.
    :fqpath_dict: fastq 路径字典
    :output_dir: 输出目录
    :threads: 线程数
    :return: None
    """
    logging.info("运行 FastQC")
    fqc_dir = output_dir / "fastqc"
    fqc_dir.mkdir(exist_ok=True, parents=True)
    # * 如果已经运行过或不是强制, 则跳过
    if not force and is_fastqc_done(fqpath_dict, fqc_dir):
        logging.warning("FastQC 已完成, 跳过")
        return
    # 单进程线程数 + 并行数
    sgl_thrd_num, prl_num = get_thread_and_parallel_number(threads)
    # 命令行列表
    cmds = []
    for samp in fqpath_dict:
        fq1 = fqpath_dict[samp]["read1"]
        fq2 = fqpath_dict[samp]["read2"]
        cmd = f"""
        source {ACTIVATE} basic
        fastqc --threads {sgl_thrd_num} --outdir {fqc_dir} {fq1} {fq2}
        conda deactivate
        """
        cmds.append(cmd)
    # 并行运行 FastQC
    multi_run_command(cmds, prl_num)


def is_fastqc_done(fqpath_dict: dict, fqc_dir: Path) -> bool:
    """
    检查 FastQC 是否完成.
    :fqpath_dict: fastq 路径字典
    :fqc_dir: FastQC 输出目录
    :return: bool
    """
    # 输入的 fastq 数量
    fqs = []
    for samp in fqpath_dict:
        for read in fqpath_dict[samp]:
            fqs.append(fqpath_dict[samp][read])
    # 跑完 FastQC 的 fastq 数量
    fqc_done_count = len(list(fqc_dir.glob('*.html')))
    if fqc_done_count == len(fqs):
        return True
    return False
