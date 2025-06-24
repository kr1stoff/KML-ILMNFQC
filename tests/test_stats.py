from pathlib import Path
from src.kml_ilmnfqc.stats import calc_fastp_stats

outdir = "/data/mengxf/Project/KML250617-ilmnfqc/work/250617"
outdir = Path(outdir)

calc_fastp_stats(outdir)
