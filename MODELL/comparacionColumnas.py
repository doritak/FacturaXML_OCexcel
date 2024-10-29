import sys
import os
import pandas as pd
# Agrega la raiz del proyecto a la ruta Python 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from CONTROLLER.importarOC import leer_oc
from CONTROLLER.importarXML import Cargar_datos_XML
from MODELL.mergeXML_OC import merge_dataframes

def comparar_columnas(df, col1, col2, diferencia):
    """
    Compare dos columnas en un DataFrame y señala las filas donde la diferencia absoluta excede un umbral especificado.    
    Parameters:
    df (pandas.DataFrame): El DataFrame que contiene las columnas a comparar.
    col1 (str): El nombre de la primera columna a comparar.
    col2 (str): El nombre de la segunda columna a comparar.
    diferencia (float): The threshold for the absolute difference between the two columns.
    nombre_col_flag (str): El umbral para la diferencia absoluta entre las dos columnas.
    Returns:
    pandas.DataFrame: El DataFrame con una columna adicional que indica si la diferencia absoluta entre col1 y col2 excede el umbral especificado.
    """
    df = df.loc[:, ["Código", col1, col2]] 
    df[col1] = df[col1].fillna(0)
    df[col2] = df[col2].fillna(0)
    df[col1] = df[col1].astype(float)
    df[col2] = df[col2].astype(float)
    nombre_col_flag = f"{col1}_dif_{col2}"
    df["diff"] = df[col1] - df[col2]
    df[nombre_col_flag] = (df[col1] - df[col2]).abs() > diferencia
    df[nombre_col_flag] = df[nombre_col_flag].apply(lambda x: 'Revisar!' if x else '')
    
    df_new = pd.DataFrame({
        "Código": df["Código"],
        col1: df[col1],
        col2: df[col2],
        "diff": df["diff"],
        nombre_col_flag: df[nombre_col_flag]
    })
    
    return df_new

def comparacion_columnas_claves(df):
    df_monto = comparar_columnas(df, "Monto_Item","TOTAL", 100)
    df_cant = comparar_columnas(df, "Cantidad","CANT", 2)
    print(df_monto)
    print(df_cant)


# Pruebas de este módulo
if __name__ == "__main__":
    archivoXML = 'XML OC Excel/../_Doc_Import/Factura.xml'
    df_XML, df_DR, df_R, nombre_proveedor = Cargar_datos_XML(archivoXML)
    
    archivoOC = 'XML OC Excel/../_Doc_Import/OC nro 6791.xlsx'
    palabraOC = 'Código'
    num_col = 14
    df_OC = leer_oc(archivoOC, palabraOC, num_col)
    
    # Tengo que hacer la comparación con el dataframe que se obtiene del merge
    df = merge_dataframes(df_XML, df_OC, 'Código')
    comparacion_columnas_claves(df)