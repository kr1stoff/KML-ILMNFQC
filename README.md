# KML-ILMNFQC

Illumina bcl2fastq 拆分后的 fastq 文件质控流程

## 用法

```bash
poetry run -C /data/mengxf/GitHub/KML-ILMNFQC python -m src.kml_ilmnfqc \
  --threads 32 \
  --input-dir /data/mengxf/Project/KML250721-tcr-RUN5/results/250721/FASTQ \
  --output-dir /data/mengxf/Project/KML250721-tcr-RUN5/results/250722-ilumnqc
```
