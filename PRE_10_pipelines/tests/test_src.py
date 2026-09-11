import os

FOLDER = "PRE_10_pipelines"
ESTIMATOR = f"{FOLDER}/submission/estimator.pkl"


def test_01():

    assert os.path.exists(ESTIMATOR)
