from pathlib import Path
from src.kml_ilmnfqc.stats import calc_fastp_stats

outdir = "/data/mengxf/Project/KML250721-tcr-RUN5/results/250722-ilumnqc"
outdir = Path(outdir)

calc_fastp_stats(outdir)
