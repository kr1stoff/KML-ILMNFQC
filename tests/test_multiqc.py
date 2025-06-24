from src.kml_ilmnfqc.multiqc import run_multiqc
from pathlib import Path


outdir = "/data/mengxf/Project/KML250617-ilmnfqc/work/250617"
outdir = Path(outdir)

run_multiqc(outdir, False)
