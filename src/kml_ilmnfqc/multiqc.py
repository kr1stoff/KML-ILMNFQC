import logging
from pathlib import Path
from subprocess import run

from src.kml_ilmnfqc.config import ACTIVATE


def run_multiqc(output_dir: Path, force: bool) -> None:
    """
    运行 MultiQC
    :param output_dir: 输出目录
    :param force: 是否强制重新运行
    """
    logging.info("运行 MultiQC")
    multiqc_outdir = output_dir / "multiqc"
    multiqc_outdir.mkdir(exist_ok=True, parents=True)
    fastqc_dir = output_dir / "fastqc"
    cmd = f"""
    source {ACTIVATE} basic
    multiqc --force --outdir {multiqc_outdir} {fastqc_dir}
    conda deactivate
    """
    if not force and multiqc_outdir.joinpath("multiqc_report.html").exists():
        logging.warning("MultiQC 已完成, 跳过")
        return
    # 执行命令
    logging.debug(f"执行命令: {cmd}")
    run(cmd, shell=True, check=True, executable="/bin/bash")
