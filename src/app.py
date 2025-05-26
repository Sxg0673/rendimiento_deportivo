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
        boton_registrar = tk.Button(self, text="Registrar Participante", command=self.abrir_formulario_registro_particiapante)
        boton_registrar.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # http://acodigo.blogspot.com/2017/03/tkinter-grid.html#google_vignette

        # Botón para ver reporte general
        btn_ver = tk.Button(self, text="Reporte General", command=self.abrir_formulario_reporte_general)
        btn_ver.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Botón para ver reporte individual
        btn_eliminar = tk.Button(self, text="Reporte Individual", command=self.abrir_formulario_reporte_individual)
        btn_eliminar.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Botón para salir y borrar base de datos
        btn_actualizar = tk.Button(self, text="Borrar Datos", command=self.salir)
        btn_actualizar.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        
    def abrir_formulario_registro_particiapante(self):
        # Configuro un venta emergente
        ventana = tk.Toplevel(self)
        ventana.title("Registrar Participante")
        ventana.geometry("400x300")

        # Creo los label y las entradas del formulario y las posiciono con grid
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
            # Confirma que todos los datos esten digitados correctamente
            nombre = entrada_nombre.get().strip()
            try:
                resistencia = float(entrada_resistencia.get())
                fuerza = float(entrada_fuerza.get())
                velocidad = float(entrada_velocidad.get())

                if not (0 <= resistencia <= 100 and 0 <= fuerza <= 100 and 0 <= velocidad <= 100):
                    raise ValueError #https://docs.python.org/es/3.13/tutorial/errors.html

                registrar_participante(nombre, resistencia, fuerza, velocidad)
                messagebox.showinfo("Éxito", "Participante registrado correctamente.")
                ventana.destroy()
            except ValueError:
                messagebox.showerror("Error", "Todos los valores deben ser números entre 0 y 100.")

        boton_guardar = tk.Button(ventana, text="Guardar", command=confirmar_registro)
        boton_guardar.grid(row=4, column=0, columnspan=2, pady=10)


    def abrir_formulario_reporte_general(self):
        # Recibo los 3 parametros que retorno en reporte_general
        df, stats, promedio = reporte_general()

        # Si no he registrado aun participantes
        if df is None:
            messagebox.showinfo("Sin datos", "No hay participantes registrados aún.")
            return

        # Ventana emergente
        ventana = tk.Toplevel(self)
        ventana.title("Reporte General")
        ventana.geometry("700x500")

        texto_tabla = tk.Text(ventana, height=10, width=80)
        texto_tabla.pack(padx=10, pady=10)

        for _, fila in df.iterrows(): #https://www-geeksforgeeks-org.translate.goog/pandas-dataframe-iterrows/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc
            estado = "Clasificó" if fila["clasifico"] else "No clasificó" # Comprobamos el valor booleano
            linea = f"{fila['nombre']} - Puntaje: {fila['puntaje_final']} → {estado}\n" # Reporte
            texto_tabla.insert(tk.END, linea) # Insertamos

        texto_stats = tk.Text(ventana, height=15, width=80)
        texto_stats.pack(padx=10, pady=10)

        texto_stats.insert(tk.END, "Estadísticas Generales:\n")
        texto_stats.insert(tk.END, stats.to_string())
        texto_stats.insert(tk.END, f"\n\nPromedio general del grupo: {round(promedio, 2)}")
    
    def abrir_formulario_reporte_individual(self):
        # Ventana emergente
        ventana = tk.Toplevel(self)
        ventana.title("Reporte Individual")
        ventana.geometry("400x200")

        # Pedimo el nombre del participante
        tk.Label(ventana, text="Nombre del participante:").grid(row=0, column=0, padx=5, pady=5)
        entrada_nombre = tk.Entry(ventana)
        entrada_nombre.grid(row=0, column=1, padx=5, pady=5)

        # Con esta funcion lo buscamos
        def buscar():
            nombre = entrada_nombre.get().strip() # Obtenemos el nombre
            datos = reporte_individual(nombre)    # Obtenemos el reporte individual de esa persona

            if datos is None: # Nos aseguramos si hay datos o sino
                messagebox.showerror("No encontrado", "No se encontró un participante con ese nombre.")
                return

            estado = "Clasificó" if datos["clasifico"] else "No clasificó" # Comrpobamos su clasificacion por medio del valor booleano
            mensaje = f"{nombre} obtuvo un puntaje final de {datos['puntaje_final']}.\nEstado: {estado}"
            messagebox.showinfo("Reporte Individual", mensaje)

        tk.Button(ventana, text="Buscar", command=buscar).grid(row=1, column=0, columnspan=2, pady=10)

    
    def salir(self): # Antes iba a ser para salir pero decidi dejarlo solo para borrar la base de datos
        confirmacion = messagebox.askyesno("Confirmar", "¿Seguro que deseas borrar la base de datos?")
        if confirmacion:
            exito = salir()
            if exito:
                messagebox.showinfo("Listo", "Base de datos eliminada correctamente.")
            else:
                messagebox.showinfo("Sin acción", "No existía una base de datos para eliminar.")
    
    
        
        

if __name__ == "__main__": # https://www.youtube.com/watch?v=wZKTUcTqekw
    app = App() # Inicializamos la clase App
    app.mainloop()
