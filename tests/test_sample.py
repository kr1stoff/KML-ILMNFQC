from pprint import pprint
from pathlib import Path

from src.kml_ilmnfqc.sample import get_sample_path_dict

indir = "/data/mengxf/Project/KML250214-lvis-YanZhengRUN3/FASTQ"
indir = Path(indir)
pprint(get_sample_path_dict(indir))
