import pandas as pd
import os
from tkinter import messagebox


def convertir_xls_a_xlsx(ruta_archivo):
    try:
        archivo_xls = pd.read_excel(ruta_archivo, engine='xlrd')
        nueva_ruta = os.path.splitext(ruta_archivo)[0] + '.xlsx'
        archivo_xls.to_excel(nueva_ruta, index=False, engine='openpyxl')
        messagebox.showinfo(
            "Éxito", f"El archivo se ha convertido a XLSX y guardado en {nueva_ruta}")
    except Exception as e:
        messagebox.showerror(
            "Error", f"No se pudo convertir el archivo a XLSX. Error: {str(e)}")


def convertir_xls_a_csv(ruta_archivo):
    try:
        archivo_xls = pd.read_excel(ruta_archivo, engine='xlrd')
        nueva_ruta = os.path.splitext(ruta_archivo)[0] + '.csv'
        archivo_xls.to_csv(nueva_ruta, index=False)
        messagebox.showinfo(
            "Éxito", f"El archivo se ha convertido a CSV y guardado en {nueva_ruta}")
    except Exception as e:
        messagebox.showerror(
            "Error", f"No se pudo convertir el archivo a CSV. Error: {str(e)}")
