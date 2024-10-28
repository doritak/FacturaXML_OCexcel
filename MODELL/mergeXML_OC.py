import pandas as pd


def merge_dataframes(df1, df2, nombre_columna):
    """
    Une dos pandas DataFrames de acuerdo a una columna específica y el resultado lo ordena por 'Nro_Linea'.
    Parameters:
    df1 (pandas.DataFrame): Primer DataFrame a unir.
    df2 (pandas.DataFrame): Segundo DataFrame a unir.
    nombre_columna (str): El nombre de la coluna que se usará para unir los DataFrames.
    Returns:
    pandas.DataFrame: El DataFrame unido y ordenado por 'Nro_Linea'.
    """
    
    merged_df = pd.merge(df1, df2, on=nombre_columna, how='outer')
    # Ordenar el DataFrame por 'Nro_Linea'
    merged_df = merged_df.sort_values(by='Nro_Linea')
    return merged_df


