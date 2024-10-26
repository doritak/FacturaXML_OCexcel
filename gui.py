import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Variables globales para almacenar rutas de archivos y una flag para indicar cancelación.
xml_file_path = ""
excel_file_path = ""
cancelado = False

def browse_xml_file():
    global xml_file_path
    file_path = filedialog.askopenfilename(filetypes=[("XML files", "*.xml")])
    if file_path:
        xml_file_path = file_path
        relative_path = os.path.relpath(file_path, start=os.path.dirname(os.path.dirname(file_path)))
        xml_path_label.config(text=relative_path)

def browse_excel_file():
    global excel_file_path
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        excel_file_path = file_path
        relative_path = os.path.relpath(file_path, start=os.path.dirname(os.path.dirname(file_path)))
        excel_path_label.config(text=relative_path)

def cancel_operation():
    global cancelado
    cancelado = True
    root.quit()
    
def process_files():
    if not xml_file_path or not excel_file_path:
        messagebox.showerror("Error", "Debe seleccionar ambos archivos: XML y Excel.")
    else:
        root.quit()

def create_gui():
    global xml_path_label, excel_path_label, root

    root = tk.Tk()
    root.title("Seleccionar los archivos a procesar")
    
    # Set custom icon for the window
    window_icon_path = 'miscelaneos/fsc.ico'  
    root.iconbitmap(window_icon_path) 
    
    # Set custom icon for the taskbar
    taskbar_icon_path = 'miscelaneos/Fsc_png.png'  # Replace with the path to your .png file
    taskbar_icon_image = tk.PhotoImage(file=taskbar_icon_path)
    root.iconphoto(True, taskbar_icon_image)
    
    # Set window size
    root.geometry("350x250")  # Set the width to 600 pixels
    
    tk.Label(root, text="Seleccionar archivo XML:").grid(row=0, column=0, padx=10, pady=10)
    tk.Button(root, text="Buscar", command=browse_xml_file).grid(row=0, column=1, padx=10, pady=10)
    xml_path_label = tk.Label(root, text="")
    xml_path_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    
    tk.Label(root, text="Seleccionar archivo Excel:").grid(row=2, column=0, padx=10, pady=10)
    tk.Button(root, text="Buscar", command=browse_excel_file).grid(row=2, column=1, padx=10, pady=10)
    excel_path_label = tk.Label(root, text="")
    excel_path_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    
    tk.Button(root, text="Procesar Archivos Seleccionados", command=process_files).grid(row=4, column=0, padx=10, pady=10)
    tk.Button(root, text="Cancelar", command=cancel_operation).grid(row=4, column=1, padx=10, pady=10)
    
    root.mainloop()

def obtener_path_archivos_seleccionados():
    return xml_file_path, excel_file_path, cancelado

if __name__ == "__main__":
    create_gui()
    