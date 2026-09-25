import pickle

from sklearn import datasets
from sklearn.svm import SVC

FOLDER = "PRE_03_clasificacion_basica_imagenes"


def cargar_datos():
    return datasets.load_digits(return_X_y=True)


def entrenar(x, y):
    clf = SVC()
    clf.fit(x, y)
    return clf


def guardar(objeto, nombre):
    with open(f"{FOLDER}/submission/{nombre}", "wb") as file:
        pickle.dump(objeto, file)


if __name__ == "__main__":
    x, y = cargar_datos()
    clf = entrenar(x, y)
    guardar(clf, "estimator.pkl")
