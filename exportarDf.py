import pandas as pd
from miscelaneos.nombrar_archivos import Nombrar_archivo
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
    # Obtener el directorio de donde estará el archivo ejecutable
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Defino el directorio donde se guardará el archivo Excel
    output_dir = os.path.join(base_dir, 'Excel_Resultado_Comparacion')
    
    # Crea el directorio si no existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Nombrar el archivo según mis parámetros
    nombre_archivo = Nombrar_archivo(proveedor,tipo)
    # Define la ruta del archivo Excel
    output_file_path = os.path.join(output_dir, nombre_archivo)
    # Exportar el DataFrame a Excel
    df.to_excel(output_file_path, index=False)
    # print(f"Archivo Excel creado exitosamente en: {nombre_archivo}")

