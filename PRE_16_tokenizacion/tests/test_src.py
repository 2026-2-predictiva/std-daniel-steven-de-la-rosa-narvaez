import os

FOLDER = "PRE_16_tokenizacion"


def test_01():

    assert os.path.exists(f"{FOLDER}/submission/file1.txt")
    assert os.path.exists(f"{FOLDER}/submission/file2.txt")
    assert os.path.exists(f"{FOLDER}/submission/file3.txt")
