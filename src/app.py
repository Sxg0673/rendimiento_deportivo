import tkinter as tk
from tkinter import messagebox

# Importamos todas las funciones necesarias desde logica.py
from logica import (
    registrar_participante,
    reporte_general,
    reporte_individual,
    salir
)

class App(tk.Tk): # Hereda la clase tk.Tk
    def __init__(self): # Constructor
        super().__init__() # Heredamos el tk.Tk

        self.title("...")
        self.geometry("500x300")
        self.resizable(True, True) # Ajustar tamaño
        
        self.configure(bg="#f5f5f5") # Color de fonod

        self.configurar_grid()
        self.crear_widgets()
        
        
    def configurar_grid(self):
        # Queremos 4 filas que se expandan proporcionalmente
        for i in range(4):
            self.grid_rowconfigure(i, weight=1)

        # Solo una columna que también se expanda
        self.grid_columnconfigure(0, weight=1)
        


    def crear_widgets(self):
        # Botón para registrar nuevo usuario
        boton_registrar = tk.Button(self, text="Registrar Participante", command=self.abrir_formulario_registro_particiapnte)
        boton_registrar.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # http://acodigo.blogspot.com/2017/03/tkinter-grid.html#google_vignette

        # Botón para ver reporte general
        btn_ver = tk.Button(self, text="Reporte General", command=self.abrir_formulario_reporte_general)
        btn_ver.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Botón para ver reporte individual
        btn_eliminar = tk.Button(self, text="Reporte Individual", command=self.abrir_formulario_reporte_individual)
        btn_eliminar.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Botón para salir y borrar base de datos
        btn_actualizar = tk.Button(self, text="Salir", command=self.salir)
        btn_actualizar.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        
    def abrir_formulario_registro_particiapnte(self):
        pass
    
    def abrir_formulario_reporte_general(self):
        pass
    
    def abrir_formulario_reporte_individual(self):
        pass
    
    def salir(self):
        pass
    
    
        
        

if __name__ == "__main__": # https://www.youtube.com/watch?v=wZKTUcTqekw
    app = App() # Inicializamos la clase App
    app.mainloop()
