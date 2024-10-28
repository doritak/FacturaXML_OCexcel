from CONTROLLER.importarXML import Cargar_datos_XML
from CONTROLLER.exportarDf import Exportar_df_excel
from CONTROLLER.importarOC import leer_oc
from MODELL.mergeXML_OC import merge_dataframes
import VIEW.gui as gui
from tkinter import messagebox

def datos_entrada():
    ruta_xml, ruta_excel, cancelado  = gui.obtener_path_archivos_seleccionados()

    if cancelado:
        print("La operación fue cancelada por el usuario.")
        return None, None
    if not ruta_xml or not ruta_excel:
        messagebox.showerror("Error", "Debe seleccionar ambos archivos: XML y Excel.")
        return None, None
    df_XML, df_DR, df_R, proveedor = Cargar_datos_XML(ruta_xml)
    
    palabra = 'Código'
    df_OC = leer_oc(ruta_excel, palabra)
    # el nombre_columna es el nombre de la columna que se va a usar para hacer el merge, en este caso es el código del producto que se encuentra tanto en la OC como en la factura
    nombre_columna = 'Código'
    df = merge_dataframes(df_XML, df_OC, nombre_columna)
  
    return df, proveedor

def Final():
    df, proveedor = datos_entrada()
    if df is None or proveedor is None:
        print("No se procesaron los archivos.")
        return
    Exportar_df_excel(df, "Detalle", proveedor)
    print("Fin del programa")


if __name__ == "__main__":
    gui.create_gui()
    Final()