import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

FOLDER = "PRE_05_clustering_demanda"
HORAS = [f"H{h:02d}" for h in range(1, 25)]


def cargar_datos():
    df = pd.read_csv(f"{FOLDER}/data/demanda_comercial.csv.zip", compression="zip")
    df["Fecha"] = pd.to_datetime(df["Fecha"])
    return df


def normalizar(df):
    datos = df[HORAS]
    return datos.div(datos.max(axis=1), axis=0)


def agrupar(perfiles, n_clusters=4):
    kmeans = KMeans(n_clusters=n_clusters, n_init=10, random_state=0)
    kmeans.fit(perfiles)
    return kmeans


def graficar_demanda(df):
    total = df[HORAS].sum(axis=1)
    plt.figure(figsize=(12, 4))
    plt.plot(df["Fecha"], total)
    plt.title("Demanda comercial diaria")
    plt.xlabel("Fecha")
    plt.ylabel("Demanda total")
    plt.tight_layout()
    plt.savefig(f"{FOLDER}/submission/demanda-comercial.png")
    plt.close()


def graficar_ejemplos(df, perfiles):
    plt.figure(figsize=(8, 5))
    for i in range(7):
        plt.plot(range(1, 25), perfiles.iloc[i], label=df["Fecha"].iloc[i].strftime("%Y-%m-%d"))
    plt.title("Patrones de demanda de ejemplo")
    plt.xlabel("Hora")
    plt.ylabel("Demanda normalizada")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{FOLDER}/submission/demanda-comercial-patrones-ejemplo.png")
    plt.close()


def graficar_perfiles(kmeans):
    plt.figure(figsize=(8, 5))
    for i, centro in enumerate(kmeans.cluster_centers_):
        plt.plot(range(1, 25), centro, label=f"Cluster {i}")
    plt.title("Perfiles de demanda por cluster")
    plt.xlabel("Hora")
    plt.ylabel("Demanda normalizada")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{FOLDER}/submission/demanda-comercial-perfiles.png")
    plt.close()


if __name__ == "__main__":
    df = cargar_datos()
    perfiles = normalizar(df)
    kmeans = agrupar(perfiles)
    graficar_demanda(df)
    graficar_ejemplos(df, perfiles)
    graficar_perfiles(kmeans)
