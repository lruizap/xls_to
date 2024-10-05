import tkinter as tk
from tkinter import filedialog, messagebox
from ..conversor import convertir_xls_a_xlsx, convertir_xls_a_csv
from .interfaz_lectura import abrir_interfaz_lectura

# Funciones de conversión


def seleccionar_archivo():
    ruta_archivo = filedialog.askopenfilename(
        title="Seleccionar archivo XLS",
        filetypes=[("Archivos XLS", "*.xls")]
    )
    if ruta_archivo:
        return ruta_archivo
    else:
        messagebox.showwarning(
            "Advertencia", "No se ha seleccionado ningún archivo.")
        return None


def convertir_a_xlsx():
    ruta_archivo = seleccionar_archivo()
    if ruta_archivo:
        convertir_xls_a_xlsx(ruta_archivo)


def convertir_a_csv():
    ruta_archivo = seleccionar_archivo()
    if ruta_archivo:
        convertir_xls_a_csv(ruta_archivo)

# Crear interfaz de conversión


def crear_interfaz_conversion():
    global ventana
    ventana = tk.Tk()
    ventana.title("Conversor de Archivos XLS")

    label = tk.Label(
        ventana, text="Seleccione el formato al que desea convertir el archivo XLS:")
    label.pack(pady=10)

    boton_xlsx = tk.Button(
        ventana, text="Convertir a XLSX", command=convertir_a_xlsx)
    boton_xlsx.pack(pady=5)

    boton_csv = tk.Button(ventana, text="Convertir a CSV",
                          command=convertir_a_csv)
    boton_csv.pack(pady=5)

    # Botón para abrir la interfaz de lectura
    boton_lectura = tk.Button(
        ventana, text="Leer Archivos", command=lambda: abrir_interfaz_lectura(ventana))
    boton_lectura.pack(pady=20)

    ventana.mainloop()
