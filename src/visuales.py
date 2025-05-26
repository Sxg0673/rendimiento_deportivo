import matplotlib.pyplot as plt
import pandas as pd

def grafico_torta(df):
    """
    Genera un gráfico de torta con el total de clasificados y no clasificados.
    """
    conteo = df['clasifico'].value_counts()
    etiquetas = ['Clasificó', 'No clasificó']
    valores = [conteo.get(True, 0), conteo.get(False, 0)]

    plt.figure()
    plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=90)
    plt.title('Participantes Clasificados vs No Clasificados')
    plt.axis('equal')
    plt.show()


def matriz_correlacion(df):
    """
    Muestra la matriz de correlación entre los puntajes.
    """
    columnas = ['resistencia', 'fuerza', 'velocidad']
    if all(col in df.columns for col in columnas):
        correlacion = df[columnas].corr()

        plt.figure()
        plt.matshow(correlacion, cmap='coolwarm')
        plt.colorbar()
        plt.title('Matriz de Correlación', pad=20)
        plt.xticks(range(len(columnas)), columnas)
        plt.yticks(range(len(columnas)), columnas)
        plt.show()
