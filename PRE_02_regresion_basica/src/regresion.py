import pickle

import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler

FOLDER = "PRE_02_regresion_basica"


def cargar_datos():
    dataset = pd.read_csv(f"{FOLDER}/data/auto_mpg.csv")
    dataset = dataset.dropna()
    dataset["Origin"] = dataset["Origin"].map({1: "USA", 2: "Europe", 3: "Japan"})
    dataset = pd.get_dummies(dataset, columns=["Origin"], prefix="", prefix_sep="")
    y = dataset.pop("MPG")
    return dataset, y


def entrenar(x, y):
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)

    mlp = MLPRegressor(hidden_layer_sizes=(64, 64), max_iter=2000, random_state=0)
    mlp.fit(x_scaled, y)
    return scaler, mlp


def guardar(objeto, nombre):
    with open(f"{FOLDER}/submission/{nombre}", "wb") as file:
        pickle.dump(objeto, file)


if __name__ == "__main__":
    x, y = cargar_datos()
    scaler, mlp = entrenar(x, y)
    guardar(scaler, "features_scaler.pkl")
    guardar(mlp, "mlp.pkl")
