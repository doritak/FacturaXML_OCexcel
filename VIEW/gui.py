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
    ventana.quit()
    
def procesar_archivos():
    if not ruta_archivo_xml or not ruta_archivo_excel:
        messagebox.showerror("Error", "Debe seleccionar ambos archivos: XML y Excel.")
    else:
        ventana.quit()

def create_gui():
    global etiqueta_ruta_xml, etiqueta_ruta_excel, ventana

    ventana = tk.Tk()
    ventana.title("Seleccionar los archivos ")
    ventana.config(bg="lightblue")
    # Establecer un icono personalizado para la ventana '../miscelaneos/fsc.ico'  
    
    ruta_icon_ventana = os.path.join(os.path.dirname(__file__), '..', 'CONTROLLER', 'miscelaneos', 'fsc.ico')
    ventana.iconbitmap(ruta_icon_ventana) 
    
    # Establecer un icono personalizado para la barra de tareas '../miscelaneos/Fsc_png.png'  
    ruta_icon_taskbar = os.path.join(os.path.dirname(__file__), '..','CONTROLLER', 'miscelaneos', 'Fsc_png.png')
    imagen_icon_taskbar = tk.PhotoImage(file=ruta_icon_taskbar)
    ventana.iconphoto(True, imagen_icon_taskbar)
    
    # Settear el tamaño de la ventana
    ventana.geometry("350x250")  
    
    tk.Label(ventana, text="Seleccionar archivo XML:", background="lightblue").grid(row=0, column=0, padx=10, pady=10)
    tk.Button(ventana, text="Buscar", command=buscar_archivo_xml).grid(row=0, column=1, padx=10, pady=10)
    etiqueta_ruta_xml = tk.Label(ventana, text="", background="lightblue")
    etiqueta_ruta_xml.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    
    tk.Label(ventana, text="Seleccionar archivo Excel:", background="lightblue").grid(row=2, column=0, padx=10, pady=10)
    tk.Button(ventana, text="Buscar", command=buscar_archivo_excel).grid(row=2, column=1, padx=10, pady=10)
    etiqueta_ruta_excel = tk.Label(ventana, text="", background="lightblue")
    etiqueta_ruta_excel.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    
    tk.Button(ventana, text="Procesar Archivos Seleccionados", command=procesar_archivos).grid(row=4, column=0, padx=10, pady=10)
    tk.Button(ventana, text="Cancelar", command=cancelar_operacion).grid(row=4, column=1, padx=10, pady=10)
    
    ventana.mainloop()

def obtener_path_archivos_seleccionados():
    return ruta_archivo_xml, ruta_archivo_excel, cancelado

if __name__ == "__main__":
    create_gui()
    