import tkinter as tk
from ..lectura import seleccionar_archivo_lectura, mostrar_contenido

# Función para abrir la interfaz de lectura


def abrir_interfaz_lectura(ventana_anterior):
    ventana_anterior.withdraw()  # Esconde la ventana anterior (de conversión)
    crear_interfaz_lectura(ventana_anterior)

# Crear interfaz de lectura


def crear_interfaz_lectura(ventana_anterior):
    ventana_lectura = tk.Toplevel()
    ventana_lectura.title("Lectura de Archivos XLS, XLSX y CSV")

    label_lectura = tk.Label(
        ventana_lectura, text="Seleccione un archivo para leer:")
    label_lectura.pack(pady=10)

    boton_cargar = tk.Button(ventana_lectura, text="Cargar archivo",
                             command=lambda: mostrar_contenido(seleccionar_archivo_lectura()))
    boton_cargar.pack(pady=5)

    # Botón para volver a la interfaz de conversión
    boton_volver = tk.Button(ventana_lectura, text="Volver a Conversor",
                             command=lambda: volver_a_conversion(ventana_lectura, ventana_anterior))
    boton_volver.pack(pady=20)


def volver_a_conversion(ventana_lectura, ventana_anterior):
    ventana_lectura.withdraw()  # Esconde la ventana de lectura
    ventana_anterior.deiconify()  # Muestra de nuevo la ventana anterior (de conversión)
