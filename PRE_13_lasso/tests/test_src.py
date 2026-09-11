import os

FOLDER = "PRE_13_lasso"
OUTPUT_FOLDER = f"{FOLDER}/submission"
ESTIMATOR = f"{OUTPUT_FOLDER}/estimator.pkl"


def test_01():

    assert os.path.exists(ESTIMATOR)
