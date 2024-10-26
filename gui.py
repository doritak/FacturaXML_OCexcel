import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Variables globales para almacenar rutas de archivos y una flag para indicar cancelación.
ruta_archivo_xml = ""
ruta_archivo_excel = ""
cancelado = False

def buscar_archivo_xml():
    global ruta_archivo_xml
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos XML", "*.xml")])
    if ruta_archivo:
        ruta_archivo_xml = ruta_archivo
        ruta_relativa = os.path.relpath(ruta_archivo, start=os.path.dirname(os.path.dirname(ruta_archivo)))
        etiqueta_ruta_xml.config(text=ruta_relativa)

def buscar_archivo_excel():
    global ruta_archivo_excel
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx")])
    if ruta_archivo:
        ruta_archivo_excel = ruta_archivo
        ruta_relativa = os.path.relpath(ruta_archivo, start=os.path.dirname(os.path.dirname(ruta_archivo)))
        etiqueta_ruta_excel.config(text=ruta_relativa)

def cancelar_operacion():
    global cancelado
    cancelado = True
    root.quit()
    
def procesar_archivos():
    if not ruta_archivo_xml or not ruta_archivo_excel:
        messagebox.showerror("Error", "Debe seleccionar ambos archivos: XML y Excel.")
    else:
        root.quit()

def create_gui():
    global etiqueta_ruta_xml, etiqueta_ruta_excel, root

    root = tk.Tk()
    root.title("Seleccionar los archivos ")
    
    # Establecer un icono personalizado para la ventana
    ruta_icon_ventana = 'miscelaneos/fsc.ico'  
    root.iconbitmap(ruta_icon_ventana) 
    
    # Establecer un icono personalizado para la barra de tareas
    ruta_icon_taskbar = 'miscelaneos/Fsc_png.png'  
    imagen_icon_taskbar = tk.PhotoImage(file=ruta_icon_taskbar)
    root.iconphoto(True, imagen_icon_taskbar)
    
    # Settear el tamaño de la ventana
    root.geometry("350x250")  
    
    tk.Label(root, text="Seleccionar archivo XML:").grid(row=0, column=0, padx=10, pady=10)
    tk.Button(root, text="Buscar", command=buscar_archivo_xml).grid(row=0, column=1, padx=10, pady=10)
    etiqueta_ruta_xml = tk.Label(root, text="")
    etiqueta_ruta_xml.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    
    tk.Label(root, text="Seleccionar archivo Excel:").grid(row=2, column=0, padx=10, pady=10)
    tk.Button(root, text="Buscar", command=buscar_archivo_excel).grid(row=2, column=1, padx=10, pady=10)
    etiqueta_ruta_excel = tk.Label(root, text="")
    etiqueta_ruta_excel.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    
    tk.Button(root, text="Procesar Archivos Seleccionados", command=procesar_archivos).grid(row=4, column=0, padx=10, pady=10)
    tk.Button(root, text="Cancelar", command=cancelar_operacion).grid(row=4, column=1, padx=10, pady=10)
    
    root.mainloop()

def obtener_path_archivos_seleccionados():
    return ruta_archivo_xml, ruta_archivo_excel, cancelado

if __name__ == "__main__":
    create_gui()
    