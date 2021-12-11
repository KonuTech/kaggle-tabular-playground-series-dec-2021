import sys
from zipfile import PyZipFile


def get_unzip(path="inputs"):
    """
    python scripts\unzip.py inputs\tabular-playground-series-dec-2021.zip
    :return:
    """
    for zip_file in sys.argv[1:]:
        pzf = PyZipFile(zip_file)
        pzf.extractall(path)

get_unzip()