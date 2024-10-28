import datetime

def Calcular_fecha(conHora, Fch=None):
    """
    Calcula la fecha actual, con o sin hora, para que sea sin hora el argumento conHora debe ser False, si es True, la fecha se entrega con la hora. Si quieres sólo una fecha cualquiera formateada, debes ingresar la fecha en formato "AAAA-MM-DD" en el argumento Fch.
    Parameters:
        conHora (bool): True si se quiere la fecha con hora "DD-MM-AAAA_T_HH_MM_SS", False si se quiere la fecha sin hora "DD-MM-AAAA".
        Fch (str, optional): Cuando quieres ingresar una fecha así "AAAA-MM-DD" y que te lo regrese formateado "DD-MM-AAAA". ESto es requerido si conHora es False.
    Returns:
    str: Retorna la fecha en formato "DD-MM-AAAA" o "DD-MM-AAAA_T_HH_MM_SS" según el argumento conHora.
    """
    
    if conHora: #Calcula la hora actual, y la entrega con la hora
        d = datetime.datetime.now()
        f = [str(d.day), str(d.month), str(d.year)]
        h = [str(d.hour), str(d.minute), str(d.second)]
        fecha = f"{'-'.join(f)}_T{'_'.join(h)}"
    else: #ingresa la fecha en formato "AAAA-MM-DD" un string
        l = Fch.split('-')
        dia = l.pop()
        mes = l.pop()
        anho = l.pop()
        l = [dia, mes, anho]
        fecha = f"{'-'.join(l)}"
    return fecha


def Nombrar_archivo(proveedor:str,tipo=None):
    """
    Genera el nombre del archivo con la fecha actual y el nombre del proveedor el argumento tipo es opcional, si se ingresa un tipo se agrega al nombre del archivo, esto sirve para diferenciar los archivos de salida        
    Parameters:
        proveedor (str): Nombre del proveedor.
        tipo (str, optional): Tipo de información, puede ser el detalle de una factura, o cualquier nombre que desee diferenciar el achivo. Defaults to None.
    Returns:
        str: Genera un nombre del tipo 'DD-MM-AAAA_tipo_Proveedor.xlsx'.
    """
    
    fecha = Calcular_fecha(True)
    nombre_tipo = f"_{tipo}_" if tipo else "_"
    nombre_archivo = fecha + nombre_tipo + proveedor.title() + '.xlsx'
    return nombre_archivo


