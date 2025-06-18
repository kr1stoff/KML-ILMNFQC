from subprocess import run
from multiprocessing import Pool
from functools import partial


def multi_run_command(cmds: list[str], prcs_num: int) -> None:
    """
    使用多线程执行一组 shell 命令.

    :param cmds: 要执行的命令列表.
    :param prcs_num: 进程数量.
    """
    _run = partial(run, shell=True, check=True, executable="/bin/bash")
    with Pool(processes=prcs_num) as pool:
        pool.map(_run, cmds)


def get_thread_and_parallel_number(total_threads: int) -> tuple[int, int]:
    """
    获取线程数和并行数. 默认情况下, 并行数为 8.
    :param total_threads: 总线程数.
    :return: 线程数和并行数.
    """
    PRL_NUM = 8
    single_thread_num = max(1, total_threads // PRL_NUM)
    return (single_thread_num, PRL_NUM)
