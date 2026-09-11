import os

FOLDER = "PRE_09_hiperparametros"


def test_01():

    assert os.path.exists(f"{FOLDER}/submission/estimator.pkl")
