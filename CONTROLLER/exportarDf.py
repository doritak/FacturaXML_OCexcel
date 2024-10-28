import pandas as pd
from CONTROLLER.miscelaneos.nombrar_archivos import Nombrar_archivo
import os

def Exportar_df_excel(df, tipo, proveedor:str):
    """
    Exporta un DataFrame a un archivo Excel en la carpeta 'Excel_Resultado_Comparacion'. Si la carpeta no existe, la crea.
    Parameters:
        df (pandas.DataFrame): El DataFrame que se desea exportar.
        tipo (str): El tipo de archivo o categoría para nombrar el archivo.
        proveedor (str): El nombre del proveedor para nombrar el archivo.
    Returns:
        None
    Side Effects:
        Crea un archivo Excel en la ruta especificada y muestra un mensaje de éxito en la consola.
    """
    # Obtener la ruta absoluta del directorio actual
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    # Subir un directorio para ir a la carpeta principal
    dir_base = os.path.dirname(directorio_actual)
    # Defino el directorio donde se guardará el archivo Excel
    dir_salida = os.path.join(dir_base, '_Excel_Resultado')
    
    # Crea el directorio si no existe
    if not os.path.exists(dir_salida):
        os.makedirs(dir_salida)
    
    # Nombrar el archivo según mis parámetros
    nombre_archivo = Nombrar_archivo(proveedor,tipo)
    # Define la ruta del archivo Excel
    ruta_archivo_salida = os.path.join(dir_salida, nombre_archivo)
    # Exportar el DataFrame a Excel
    df.to_excel(ruta_archivo_salida, index=False)
    # print(f"Archivo Excel creado exitosamente en: {nombre_archivo}")

