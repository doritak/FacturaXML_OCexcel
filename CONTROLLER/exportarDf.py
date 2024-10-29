import sys
import os
import pandas as pd
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from CONTROLLER.miscelaneos.nombrar_archivos import Nombrar_archivo


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
    
    # Obtener el directorio donde está el ejecutable (o script, si se ejecuta como script)
    if getattr(sys, 'frozen', False):
        # Si es un ejecutable
        directorio_base = os.path.dirname(sys.executable)
    else:
        # Si se ejecuta como script de Python
        directorio_base = os.path.dirname(os.path.abspath(__file__))  
    # Crear el directorio de salida relativo al directorio del ejecutable
    dir_salida = os.path.join(directorio_base,"..", "_Excel_Resultado")

    
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

