from exportarDf import Exportar_df_excel 
from importarXML import Cargar_datos_XML
#AQUI sólamente para pruebas de que entrega bien los excel de los dataframes de los XML
#FUNCIONA BIEN! .... despues de todo, no funciono, pq hice muchos cambios, este archivo, pero el main.py funciona perfecto!
def Entregar_DataFrames_DTE(ruta_xml):
    df, df_DR, df_R, proveedor = Cargar_datos_XML(ruta_xml)
    
    Exportar_df_excel(df,"Detalle", proveedor)
    
    if not df_DR.empty:
        Exportar_df_excel(df_DR,"DescRecargo", proveedor)
    
    if not df_R.empty:
        Exportar_df_excel(df_R,"Referencia", proveedor)

if __name__ == "__main__":
    Entregar_DataFrames_DTE("Doc_Import/Factura.xml")