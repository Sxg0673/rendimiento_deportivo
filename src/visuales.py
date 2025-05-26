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

def histograma_puntajes(datos):
    """
    Genera un histograma con los puntajes en resistencia, fuerza y velocidad
    de un participante específico.
    
    - Recibe un diccionario con los datos del participante.
    - Usa matplotlib para mostrar el gráfico.
    """
    puntajes = {
        'Resistencia': datos['resistencia'],
        'Fuerza': datos['fuerza'],
        'Velocidad': datos['velocidad']
    }

    categorias = list(puntajes.keys())           # ['Resistencia', 'Fuerza', 'Velocidad']
    valores = list(puntajes.values())            # [78, 65, 90] por ejemplo

    plt.figure(figsize=(6, 4))                   # Define el tamaño del gráfico
    plt.bar(categorias, valores, color='skyblue')# Crea las barras
    plt.ylim(0, 100)                             # Fija el rango vertical (0 a 100)
    plt.title('Puntajes por Prueba')             # Título del gráfico
    plt.ylabel('Puntaje')                        # Etiqueta del eje Y
    plt.xlabel('Pruebas')                        # Etiqueta del eje X
    plt.tight_layout()                           # Ajusta el diseño para que no se corte
    plt.show()                                   # Muestra el gráfico

def histograma_dificultades(datos):
    """
    Genera un histograma con las dificultades aplicadas en cada prueba 
    (resistencia, fuerza y velocidad) para un participante específico.

    - Recibe un diccionario con los datos del participante.
    - Muestra el gráfico usando matplotlib.
    """
    dificultades = {
        'Resistencia': datos['dificultad_resistencia'],
        'Fuerza': datos['dificultad_fuerza'],
        'Velocidad': datos['dificultad_velocidad']
    }

    categorias = list(dificultades.keys())
    valores = list(dificultades.values())

    plt.figure(figsize=(6, 4))
    plt.bar(categorias, valores, color='orange')
    plt.ylim(1.0, 1.3)
    plt.title('Dificultades por Prueba')
    plt.ylabel('Dificultad')
    plt.xlabel('Pruebas')
    plt.tight_layout()
    plt.show()

def histograma_ponderados(datos):
    """
    Genera un histograma con los puntajes ponderados (puntaje × dificultad)
    en cada prueba para un participante específico.

    - Recibe un diccionario con los datos del participante.
    - Calcula el puntaje ponderado en resistencia, fuerza y velocidad.
    - Muestra el gráfico usando matplotlib.
    """
    ponderados = {
        'Resistencia': datos['resistencia'] * datos['dificultad_resistencia'],
        'Fuerza': datos['fuerza'] * datos['dificultad_fuerza'],
        'Velocidad': datos['velocidad'] * datos['dificultad_velocidad']
    }

    categorias = list(ponderados.keys())
    valores = list(ponderados.values())

    plt.figure(figsize=(6, 4))
    plt.bar(categorias, valores, color='seagreen')
    plt.ylim(0, 130)
    plt.title('Puntajes Ponderados por Prueba')
    plt.ylabel('Puntaje Ponderado')
    plt.xlabel('Pruebas')
    plt.tight_layout()
    plt.show()
