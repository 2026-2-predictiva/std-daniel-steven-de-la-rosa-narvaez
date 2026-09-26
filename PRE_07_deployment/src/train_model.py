import os
import pickle

import pandas as pd  # type: ignore
from sklearn.linear_model import LinearRegression  # type: ignore

FOLDER = "PRE_07_deployment"

df = pd.read_csv(f"{FOLDER}/data/house_data.csv")

features = df[
    [
        "bedrooms",
        "bathrooms",
        "sqft_living",
        "sqft_lot",
        "floors",
        "waterfront",
        "condition",
    ]
]

target = df[["price"]]

estimator = LinearRegression()
estimator.fit(features, target)


with open(f"{FOLDER}/submission/house_predictor.pkl", "wb") as file:
    pickle.dump(estimator, file)