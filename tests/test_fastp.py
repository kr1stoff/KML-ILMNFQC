from pathlib import Path

from src.kml_ilmnfqc.fastp import run_fastp, is_fastp_done
from src.kml_ilmnfqc.sample import get_sample_path_dict

indir = "/data/mengxf/Project/KML250214-lvis-YanZhengRUN3/FASTQ"
indir = Path(indir)
outdir = "/data/mengxf/Project/KML250617-ilmnfqc/work/250617"
outdir = Path(outdir)
threads = 32

fqpathdict = get_sample_path_dict(indir)
# print(is_fastp_done(fqpathdict, outdir / "fastp"))
run_fastp(fqpathdict, outdir, threads, False)
