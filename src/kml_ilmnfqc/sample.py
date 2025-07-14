import logging
from pathlib import Path


def get_sample_path_dict(input_dir: Path) -> dict[str, dict[str, str]]:
    """
    获取样本路径字典
    :input_dir: 输入文件夹路径
    """
    logging.info(f"获取样本路径字典.")
    # 检查输入文件夹是否存在
    if not input_dir.is_dir():
        raise ValueError(f"{input_dir} 不存在或不是一个文件夹!")
    # 遍历输入文件夹中的所有 fastq 文件，并将其添加到样本路径字典中
    sample_path_dict = {}
    for fq in input_dir.glob("*.fastq.gz"):
        # * 使用 _ 兼容更多 fastq 文件名格式
        name = fq.name.split("_")[0]
        if "Undetermined" == name:
            logging.debug(f"跳过未拆分的 Undetermined fastq: {name}.")
            continue
        sample_path_dict.setdefault(name, {})
        if "R1" in fq.name:
            sample_path_dict[name].update({'read1': fq})
        elif "R2" in fq.name:
            sample_path_dict[name].update({'read2': fq})
        else:
            raise ValueError(f"{fq} 不是有效的 fastq 文件.")
    return sample_path_dict

# * 后续添加单端测序, 字典只包含 dict['sample']['read1']
