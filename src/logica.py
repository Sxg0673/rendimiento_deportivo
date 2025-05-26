import random
import csv
import math
import os
import pandas as pd

from visuales import ( # importar funciones gráficas
    grafico_torta,
    matriz_correlacion,
    histograma_puntajes,
    histograma_dificultades,
    histograma_dificultades,
    histograma_ponderados
)

# Ruta del archivo CSV que almacenará los proyectos
ARCHIVO_CSV = 'data/participantes.csv'

def registrar_participante(nombre, r_resistencia, r_fuerza, r_velocidad):
    """
    Registra un nuevo participante en el archivo CSV.

    - Recibe el nombre del participante y sus puntajes en tres pruebas físicas: 
      resistencia, fuerza y velocidad (valores entre 0 y 100).
    - Genera una dificultad aleatoria (entre 1.0 y 1.3) para cada prueba.
    - Calcula el puntaje final ponderado con la fórmula:

        Puntaje Final = (∑ puntaje x dificultad) / ∑ dificultades

    - Redondea el puntaje final a un número entero.
    - Determina si el participante clasifica (puntaje >= 70).
    - Guarda todos los datos en el archivo 'participantes.csv'.
    """
    
    # Genera dificultad aleatoria entre 1.0 y 1.3
    dificultad_resistencia = random.uniform(1.0, 1.3) 
    dificultad_fuerza = random.uniform(1.0, 1.3)
    dificultad_velocidad = random.uniform(1.0, 1.3)
    
    # Total categoria ponderada
    total_resistencia = dificultad_resistencia * r_resistencia
    total_fuerza = dificultad_fuerza * r_fuerza
    total_velocidad = dificultad_velocidad * r_velocidad
    
    # Sumatorias
    suma_puntajes = total_resistencia + total_fuerza + total_velocidad
    suma_dificultades =  dificultad_resistencia + dificultad_fuerza + dificultad_velocidad
    
    # Puntaje final
    puntaje_final = round(suma_puntajes / suma_dificultades)
    
    # Determinacion de la clasificacion del participante
    if puntaje_final >= 70:
        clasifico = True
    else:
        clasifico = False
        
    # Diccionario con todos los datos del participante
    fila = {
        'nombre': nombre,
        'resistencia': r_resistencia,
        'fuerza': r_fuerza,
        'velocidad': r_velocidad,
        'dificultad_resistencia': round(dificultad_resistencia, 2),
        'dificultad_fuerza': round(dificultad_fuerza, 2),
        'dificultad_velocidad': round(dificultad_velocidad, 2),
        'puntaje_final': puntaje_final,
        'clasifico': clasifico
    }
    
    # Verifica si el archivo ya existe
    archivo_existe = os.path.isfile(ARCHIVO_CSV)

    # Abre el archivo para escritura
    with open(ARCHIVO_CSV, mode='a', newline='') as f: # Este fragmento es el mismo de la tarea pasada
        writer = csv.DictWriter(f, fieldnames=fila.keys())
        if not archivo_existe:
            writer.writeheader()
        writer.writerow(fila)

      
    
def reporte_general():
    """
    Genera los elementos del reporte general:
    - Retorna DataFrame con nombre, puntaje final y clasificación.
    - Llama funciones gráficas para torta y correlación.
    """
    
    # Intentamos leer el archivo
    try:
        df = pd.read_csv(ARCHIVO_CSV)
    except FileNotFoundError:
        return None, None, None #tres valores porque abajo tambien devolvemos 3


    # Calcular estadísticas
    estadisticas = df[['resistencia', 'fuerza', 'velocidad', 'puntaje_final']].describe()
    promedio_general = df['puntaje_final'].mean()
    
    # Llamamos a las gráficas
    grafico_torta(df)
    matriz_correlacion(df)
    

    # Retornamos lo que se nos pide para la GUI
    return df[['nombre', 'puntaje_final', 'clasifico']], estadisticas, promedio_general
    
    
    
    

def reporte_individual(nombre):
    """
    Genera un reporte individual de un participante específico.

    - Recibe el nombre del participante a consultar.
    - Busca sus datos en el archivo 'participantes.csv'.
    - Muestra su puntaje final y estado de clasificación.
    - Genera tres histogramas:
        1. Puntajes en resistencia, fuerza y velocidad.
        2. Dificultad aplicada en cada prueba.
        3. Puntaje ponderado por prueba.
    """
    try:
        df = pd.read_csv(ARCHIVO_CSV)
    except FileNotFoundError:
        return None
    
    # Filtrar por nombre (caso insensible)
    participante = df[df['nombre'].str.lower() == nombre.lower()]

    if participante.empty:
        return None

    # Convertir a diccionario para retorno y graficación
    datos = participante.iloc[0].to_dict()

    # Llamar a funciones gráficas
    histograma_puntajes(datos)
    histograma_dificultades(datos)
    histograma_ponderados(datos)

    return datos
    
def salir():
    """
    Elimina el archivo 'participantes.csv' si existe.

    - Se ejecuta al seleccionar la opción 'Salir' desde la interfaz gráfica.
    - Borra la base de datos para reiniciar el sistema en la próxima ejecución.
    - Se confirmara esta acción desde la GUI antes de ejecutarla.
    """
    pass