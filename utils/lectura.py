import pandas as pd
from tkinter import filedialog, messagebox, Text, Scrollbar, Toplevel


def seleccionar_archivo_lectura():
    ruta_archivo = filedialog.askopenfilename(
        title="Seleccionar archivo para lectura",
        filetypes=[("Archivos XLSX, XLS y CSV", "*.xlsx *.xls *.csv")]
    )
    if ruta_archivo:
        return ruta_archivo
    else:
        messagebox.showwarning(
            "Advertencia", "No se ha seleccionado ningún archivo.")
        return None


def mostrar_contenido(ruta_archivo):
    try:
        # Leer el archivo según su extensión
        if ruta_archivo.endswith('.xlsx') or ruta_archivo.endswith('.xls'):
            df = pd.read_excel(ruta_archivo)
        elif ruta_archivo.endswith('.csv'):
            df = pd.read_csv(ruta_archivo)
        else:
            messagebox.showerror("Error", "Formato de archivo no soportado.")
            return

        # Crear ventana nueva para mostrar contenido
        ventana_lectura = Toplevel()
        ventana_lectura.title("Contenido del archivo")

        # Crear una caja de texto con scroll para mostrar los datos
        text_box = Text(ventana_lectura, wrap="none")
        text_box.pack(expand=True, fill='both')

        # Scroll horizontal y vertical
        scroll_y = Scrollbar(
            ventana_lectura, orient='vertical', command=text_box.yview)
        scroll_y.pack(side="right", fill="y")
        text_box.config(yscrollcommand=scroll_y.set)

        # Mostrar las primeras filas del archivo (head)
        text_box.insert("end", df.head().to_string())
        # Hacer la caja de texto de solo lectura
        text_box.config(state="disabled")
    except Exception as e:
        messagebox.showerror("Error", f"Error al leer el archivo: {str(e)}")
