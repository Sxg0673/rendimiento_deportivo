# Sistema de Gestión de Rendimiento Deportivo

Aplicación desarrollada en Python con interfaz gráfica (Tkinter), que permite registrar, analizar y reportar el rendimiento de participantes en tres pruebas físicas:

- **Resistencia**
- **Fuerza**
- **Velocidad**

El sistema calcula un puntaje final ponderado usando dificultades aleatorias en cada prueba, y determina si cada participante clasifica o no clasifica.

---

## Funcionalidades

1. Registrar participante con puntajes y dificultades aleatorias.
2. Mostrar reporte general con estadísticas (pandas), torta de clasificación y matriz de correlación.
3. Mostrar reporte individual con histogramas por prueba.
4. Interfaz desarrollada en Tkinter, fácil de usar.

---

## Tecnologías utilizadas

- Python 3.11
- Tkinter
- Pandas
- Matplotlib

---

## Estructura del Proyecto

rendimiento_deportivo/
├── src/
│ ├── app.py # Interfaz gráfica
│ ├── logica.py # Clases y lógica del sistema
│ ├── visuales.py # Gráficos y reportes
├── data/ # Archivos de datos (participants.csv)
├── .gitignore
└── README.md


