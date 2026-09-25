import pickle

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

FOLDER = "PRE_04_clasificacion_basica_texto"


def cargar_datos():
    dataframe = pd.read_csv(
        f"{FOLDER}/data/sentences.csv.zip",
        index_col=False,
        compression="zip",
    )
    return dataframe.phrase, dataframe.target


def entrenar(frases, y):
    vectorizer = CountVectorizer()
    x = vectorizer.fit_transform(frases)

    clf = LogisticRegression(max_iter=1000)
    clf.fit(x, y)
    return vectorizer, clf


def guardar(objeto, nombre):
    with open(f"{FOLDER}/submission/{nombre}", "wb") as file:
        pickle.dump(objeto, file)


if __name__ == "__main__":
    frases, y = cargar_datos()
    vectorizer, clf = entrenar(frases, y)
    guardar(vectorizer, "vectorizer.pkl")
    guardar(clf, "clf.pkl")
