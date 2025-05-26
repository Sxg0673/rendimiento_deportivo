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
        ventana = tk.Toplevel(self)
        ventana.title("Registrar Participante")
        ventana.geometry("400x300")

        tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entrada_nombre = tk.Entry(ventana)
        entrada_nombre.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(ventana, text="Resistencia (0-100):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        entrada_resistencia = tk.Entry(ventana)
        entrada_resistencia.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(ventana, text="Fuerza (0-100):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        entrada_fuerza = tk.Entry(ventana)
        entrada_fuerza.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(ventana, text="Velocidad (0-100):").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        entrada_velocidad = tk.Entry(ventana)
        entrada_velocidad.grid(row=3, column=1, padx=5, pady=5)

        def confirmar_registro():
            nombre = entrada_nombre.get().strip()
            try:
                resistencia = float(entrada_resistencia.get())
                fuerza = float(entrada_fuerza.get())
                velocidad = float(entrada_velocidad.get())

                if not (0 <= resistencia <= 100 and 0 <= fuerza <= 100 and 0 <= velocidad <= 100):
                    raise ValueError

                registrar_participante(nombre, resistencia, fuerza, velocidad)
                messagebox.showinfo("Éxito", "Participante registrado correctamente.")
                ventana.destroy()
            except ValueError:
                messagebox.showerror("Error", "Todos los valores deben ser números entre 0 y 100.")

        boton_guardar = tk.Button(ventana, text="Guardar", command=confirmar_registro)
        boton_guardar.grid(row=4, column=0, columnspan=2, pady=10)


    def abrir_formulario_reporte_general(self):
        df, stats, promedio = reporte_general()

        if df is None:
            messagebox.showinfo("Sin datos", "No hay participantes registrados aún.")
            return

        ventana = tk.Toplevel(self)
        ventana.title("Reporte General")
        ventana.geometry("700x500")

        texto_tabla = tk.Text(ventana, height=10, width=80)
        texto_tabla.pack(padx=10, pady=10)

        for _, fila in df.iterrows():
            estado = "Clasificó" if fila["clasifico"] else "No clasificó"
            linea = f"{fila['nombre']} - Puntaje: {fila['puntaje_final']} → {estado}\n"
            texto_tabla.insert(tk.END, linea)

        texto_stats = tk.Text(ventana, height=15, width=80)
        texto_stats.pack(padx=10, pady=10)

        texto_stats.insert(tk.END, "Estadísticas Generales:\n")
        texto_stats.insert(tk.END, stats.to_string())
        texto_stats.insert(tk.END, f"\n\nPromedio general del grupo: {round(promedio, 2)}")
    
    def abrir_formulario_reporte_individual(self):
        ventana = tk.Toplevel(self)
        ventana.title("Reporte Individual")
        ventana.geometry("400x200")

        tk.Label(ventana, text="Nombre del participante:").grid(row=0, column=0, padx=5, pady=5)
        entrada_nombre = tk.Entry(ventana)
        entrada_nombre.grid(row=0, column=1, padx=5, pady=5)

        def buscar():
            nombre = entrada_nombre.get().strip()
            datos = reporte_individual(nombre)

            if datos is None:
                messagebox.showerror("No encontrado", "No se encontró un participante con ese nombre.")
                return

            estado = "Clasificó" if datos["clasifico"] else "No clasificó"
            mensaje = f"{nombre} obtuvo un puntaje final de {datos['puntaje_final']}.\nEstado: {estado}"
            messagebox.showinfo("Reporte Individual", mensaje)

        tk.Button(ventana, text="Buscar", command=buscar).grid(row=1, column=0, columnspan=2, pady=10)

    
    def salir(self):
        pass
    
    
        
        

if __name__ == "__main__": # https://www.youtube.com/watch?v=wZKTUcTqekw
    app = App() # Inicializamos la clase App
    app.mainloop()
