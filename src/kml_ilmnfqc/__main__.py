import logging

from src.kml_ilmnfqc.cli import main


logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    main()
