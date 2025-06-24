import logging
from pathlib import Path

from src.kml_ilmnfqc.util import get_thread_and_parallel_number, multi_run_command
from src.kml_ilmnfqc.config import FASTP


def run_fastp(fqpath_dict: dict, output_dir: Path, threads: int, force: bool = False):
    """
    使用 fastp 进行快速质量评估

    :param fqpath_dict: 样本路径字典
    :param output_dir: 输出目录
    :param threads: 线程数
    :param force: 是否强制重新运行
    """
    logging.info("运行 fastp")
    fastp_dir = output_dir / "fastp"
    fastp_dir.mkdir(exist_ok=True, parents=True)
    # 检查 fastp 是否完成
    if not force and is_fastp_done(fqpath_dict, fastp_dir):
        logging.warning("fastp 已完成, 跳过")
        return
    # 单进程线程数 + 并行数
    sgl_thrd_num, prl_num = get_thread_and_parallel_number(threads)
    # 命令行列表
    cmds = []
    for samp in fqpath_dict:
        fq1 = fqpath_dict[samp]["read1"]
        fq2 = fqpath_dict[samp]["read2"]
        cmd = f"""
        {FASTP} --thread {sgl_thrd_num} \
            -i {fq1} -I {fq2} \
            -o {fastp_dir}/{samp}.clean.1.fastq.gz -O {fastp_dir}/{samp}.clean.2.fastq.gz \
            --html {fastp_dir}/{samp}.html \
            --json {fastp_dir}/{samp}.json
        rm -f {fastp_dir}/{samp}.clean.1.fastq.gz {fastp_dir}/{samp}.clean.2.fastq.gz
        """
        cmds.append(cmd)
    # 并行运行 fastp
    multi_run_command(cmds, prl_num)


def is_fastp_done(fqpath_dict: dict, fastp_dir: Path) -> bool:
    """
    检查 fastp 是否完成

    :param fqpath_dict: fastq 路径字典
    :param fastp_dir: fastp 输出目录
    :return: bool
    """
    # 跑完 fastp 的 fastq 数量
    fastp_done_count = len(list(fastp_dir.glob('*.json')))
    if fastp_done_count == len(fqpath_dict.keys()):
        return True
    return False
