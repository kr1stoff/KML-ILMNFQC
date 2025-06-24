import logging
from pathlib import Path
import json
import pandas as pd
import numpy as np


def calc_fastp_stats(outdir: Path):
    """
    Generate a summary table from multiple fastp JSON files.
    从多样本 fastp JSON 文件生成一个汇总表
    :param outdir: 输出目录
    :return: None
    """
    logging.info("计算 fastp 统计信息")
    files_fastp_json = outdir.glob("fastp/*.json")
    outfile = outdir / "summary.tsv"
    # 质控表格内容
    title = ["Sample", "RawReads", "RawBases", "CleanReads", "CleanBases", "RawQ20",
             "RawQ30", "CleanQ20", "CleanQ30", "CleanAverageLength", "GC"]
    df = pd.DataFrame(columns=title)
    for js_path in files_fastp_json:
        js_data = json.loads(open(js_path, "r").read())
        sample = Path(js_path).stem
        mean_lengths = np.array(
            [v for k, v in js_data["summary"]["after_filtering"].items() if k.endswith("mean_length")])
        out = [
            sample,
            js_data["summary"]["before_filtering"]["total_reads"],
            js_data["summary"]["before_filtering"]["total_bases"],
            js_data["summary"]["after_filtering"]["total_reads"],
            js_data["summary"]["after_filtering"]["total_bases"],
            js_data["summary"]["before_filtering"]["q20_rate"],
            js_data["summary"]["before_filtering"]["q30_rate"],
            js_data["summary"]["after_filtering"]["q20_rate"],
            js_data["summary"]["after_filtering"]["q30_rate"],
            int(mean_lengths.mean()),
            js_data["summary"]["after_filtering"]["gc_content"],
        ]
        df.loc[len(df)] = out
    df.to_csv(outfile, index=False, sep="\t")
