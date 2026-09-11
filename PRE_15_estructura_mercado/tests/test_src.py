import os

FOLDER = "PRE_15_estructura_mercado"


def test_01():

    assert os.path.exists(f"{FOLDER}/submission/stocks.png")
