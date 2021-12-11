import sys
from zipfile import PyZipFile


def get_unzip(path="inputs"):
    """

    :return:
    """
    for zip_file in sys.argv[1:]:
        pzf = PyZipFile(zip_file)
        pzf.extractall(path)

get_unzip()