import pandas as pd
from importarXML import Cargar_datos_XML, Nombrar_archivo, Exportar_df_excel
from leerOC import leer_oc


def merge_dataframes(df1, df2, nombre_columna):
    merged_df = pd.merge(df1, df2, on=nombre_columna, how='outer')
    return merged_df

def compare_columnas(df, col1, col2, diferencia, nombre_col_flag):
    df[col1] = df[col1].fillna(0)
    df[col2] = df[col2].fillna(0)
    df[col1] = df[col1].astype(float)
    df[col2] = df[col2].astype(float)
    nombre_col_flag = f"{col1}_dif_{col2}"
    df[nombre_col_flag] = (df[col1] - df[col2]).abs() > diferencia
    df[nombre_col_flag] = df[nombre_col_flag].apply(lambda x: 'Revisar!' if x else '')
    return df

def datos_entrada():
    ruta_xml = "Factura.xml"
    df_XML, df_DR, df_R, proveedor = Cargar_datos_XML(ruta_xml)
    
    archivo = 'OC nro 6791 - Patricio Lioi.xlsx'
    palabra = 'Código'
    df_OC = leer_oc(archivo, palabra)
    
    nombre_columna = 'Código'
    df = merge_dataframes(df_XML, df_OC, nombre_columna)
    
    # Ordenar el DataFrame por 'Nro_Linea'
    df = df.sort_values(by='Nro_Linea')
    return df, proveedor

def revisar_diferencias_en_col(df):
    # Aqui tengo que comparar las columunas, cantidades, precios, monto final
    # el problema que no estoy segura del nombre de las columnas en las OC de excel
    pass


if __name__ == '__main__':
    df, proveedor = datos_entrada()
    Exportar_df_excel(df, "Detalle", proveedor)
    print("Fin del programa")
