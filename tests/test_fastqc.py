from pathlib import Path

from src.kml_ilmnfqc.fastqc import run_fastqc, is_fastqc_done
from src.kml_ilmnfqc.sample import get_sample_path_dict

indir = "/data/mengxf/Project/KML250214-lvis-YanZhengRUN3/FASTQ"
outdir = "/data/mengxf/Project/KML250617-ilmnfqc/work/250617"

indir = Path(indir)
outdir = Path(outdir)
threads = 32
fqptdict = get_sample_path_dict(indir)

# run_fastqc(fqptdict, outdir, threads, False)
print(is_fastqc_done(fqptdict, outdir / "fastqc"))
