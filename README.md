# Conversor y Lector de Archivos XLS, XLSX y CSV

Este proyecto es una aplicación basada en `tkinter` para realizar dos funciones principales:

1. **Convertir archivos `.xls` a `.xlsx` o `.csv`.**
2. **Leer archivos `.xls`, `.xlsx` y `.csv` y mostrar su contenido usando `pandas`.**

La interfaz del programa está dividida en dos partes:

- Una para la **conversión de archivos**.
- Otra para la **lectura de archivos**.

## Estructura del proyecto

```

.
├── documents
├── utils
│   ├── interfaz
│   │   ├──   interfaz_conversion.py         # Interfaz gráfica para convertir archivos
│   │   ├── interfaz_lectura.py              # Interfaz gráfica para leer archivos
│   ├── conversor.py                         # Funciones para convertir archivos .xls a .xlsx o .csv
│   ├── lectura.py                           # Funciones para leer archivos y mostrarlos con pandas
├── main.py                                  # Archivo principal que inicia la aplicación
├── requirements.txt                         # Archivo con las dependencias necesarias
└── README.md                                # Instrucciones y descripción del proyecto


```

## Requisitos

Para ejecutar este proyecto, debes tener instaladas todas las dependencias indicadas en `requirements.txt`.

### Dependencias principales

- `pandas`: Para el manejo de archivos `.xls`, `.xlsx`, y `.csv`.
- `xlrd`: Para leer archivos `.xls`.
- `openpyxl`: Para escribir y leer archivos `.xlsx`.
- `tkinter`: Para la interfaz gráfica.

Asegúrate de tener todas las dependencias instaladas ejecutando:

```bash
pip install -r requirements.txt
```

## Uso del programa

### 1. Conversión de archivos `.xls` a `.xlsx` o `.csv`

1. Ejecuta el archivo principal `main.py`:

   ```bash
   python main.py
   ```

2. Se abrirá una interfaz de usuario con opciones para convertir un archivo `.xls` a formato `.xlsx` o `.csv`.

3. Selecciona el archivo `.xls` que deseas convertir y elige el formato de conversión deseado.

4. Se generará un archivo en el formato seleccionado en la misma ubicación que el archivo original.

### 2. Lectura de archivos `.xls`, `.xlsx` o `.csv`

1. Desde la misma interfaz de conversión, puedes hacer clic en el botón **"Leer Archivos"**.

2. Esto abrirá una nueva ventana donde podrás seleccionar un archivo de tipo `.xls`, `.xlsx` o `.csv`.

3. Una vez seleccionado el archivo, la aplicación mostrará las primeras filas del archivo (similares a `pandas.DataFrame.head()`).

4. Puedes volver a la interfaz de conversión presionando el botón **"Volver a Conversor"**.

## Estructura del código

### 1. `conversor.py`

Contiene las funciones:

- `convertir_xls_a_xlsx()`: Convierte un archivo `.xls` a `.xlsx`.
- `convertir_xls_a_csv()`: Convierte un archivo `.xls` a `.csv`.

### 2. `lectura.py`

Contiene las funciones:

- `seleccionar_archivo_lectura()`: Permite seleccionar un archivo `.xls`, `.xlsx`, o `.csv` para lectura.
- `mostrar_contenido()`: Lee y muestra las primeras filas del archivo seleccionado.

### 3. `interfaz_conversion.py`

Maneja la interfaz gráfica para la conversión de archivos con botones para seleccionar el archivo y convertirlo, así como para acceder a la interfaz de lectura.

### 4. `interfaz_lectura.py`

Maneja la interfaz gráfica para la lectura de archivos con botones para seleccionar el archivo y mostrar su contenido. También incluye un botón para regresar a la interfaz de conversión.

### 5. `main.py`

Es el archivo principal que inicializa la interfaz de conversión.

## Licencia

Este proyecto está disponible bajo la licencia MIT. Consulta el archivo `LICENSE` para obtener más información.

---

¡Gracias por usar este programa! Si tienes alguna duda o encuentras algún error, no dudes en abrir un *issue* o contribuir con mejoras.
