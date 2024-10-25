import pandas as pd
import xml.etree.ElementTree as ET
import datetime
############# Voy a necesitar esta desde otro módulo ################
############ Cargar_datos_XML(ruta_xml)->df, df_DR, df_R, nombre_proveedor
def Cargar_datos_XML(ruta_xml):
    # Debo especificar el encoding al abrir el archivo
    with open(ruta_xml, encoding='ISO-8859-1') as file:
        tree = ET.parse(file)
        root = tree.getroot()
    
    # Definir el espacio de nombres
    nsp  = {'ns': 'http://www.sii.cl/SiiDte'}
    # Debo validar la estructura del XML pq no encuentro el Document
    # tener cuidado, me faltaba el namespace del SII... jej3
    # def imprimir_estructura(elemento, nivel=0):
    #     espaciado = '  ' * nivel
    #     print(f"{espaciado}{elemento.tag}")
    #     for hijo in elemento:
    #         imprimir_estructura(hijo, nivel+ 1)
    # imprimir_estructura(root)

    # Navegar por la estructura: EnvioDTE > SetDTE > DTE > Documento
    documento = root.find('.//ns:Documento', namespaces=nsp )
    if documento is None:
        raise ValueError("No se encontró el nodo 'Documento' en el XML.")
    # Extraer Datos del proveedor
    nombre_proveedor = documento.find('ns:Encabezado', namespaces=nsp).find('ns:Emisor', namespaces=nsp).find('ns:RznSoc', namespaces=nsp).text
    Folio = int(documento.find('ns:Encabezado', namespaces=nsp).find('ns:IdDoc', namespaces=nsp).find('ns:Folio', namespaces=nsp).text)
    FechaEmis = documento.find('ns:Encabezado', namespaces=nsp).find('ns:IdDoc', namespaces=nsp).find('ns:FchEmis', namespaces=nsp).text
    FechaEmis = Calcular_fecha(False, FechaEmis)
    RUT = documento.find('ns:Encabezado', namespaces=nsp).find('ns:Emisor', namespaces=nsp).find('ns:RUTEmisor', namespaces=nsp).text
    FechaEmis = Calcular_fecha(False, FechaEmis)
    
    # print(nombre_proveedor, Folio,FechaEmis )
    # Extraer datos de cada "detalle" dentro del documento, incluyendo el namespace"
    data = []
    for detalle in documento.findall('ns:Detalle', namespaces=nsp):
        # Verificar que 'CdgItem' existe en cada 'detalle'
        codigo_prod = detalle.find('ns:CdgItem', namespaces=nsp)
        if codigo_prod is not None:
            codigo = codigo_prod.find('ns:VlrCodigo', namespaces=nsp)
            # Verificar que 'codigo' existe y obtener su texto
            SKU = codigo.text if codigo is not None else 'N/A'
        else:
            SKU = 'N/A'  # Valor por defecto si no hay 'codigo_prod'
        # aquí extraje el número de línea del detalle de productos
        NroLin = int(detalle.find('ns:NroLinDet', namespaces=nsp).text) if detalle.find('ns:NroLinDet', namespaces=nsp) is not None else 0
        # Extraer los otros campos
        nombre_prod = detalle.find('ns:NmbItem', namespaces=nsp).text if detalle.find('ns:NmbItem', namespaces=nsp) is not None else 'N/A'
        cantidad = float(detalle.find('ns:QtyItem', namespaces=nsp).text) if detalle.find('ns:QtyItem', namespaces=nsp) is not None else 0.0
        precio = float(detalle.find('ns:PrcItem', namespaces=nsp).text) if detalle.find('ns:PrcItem', namespaces=nsp) is not None else 0.0
        descuento = float(detalle.find('ns:DescuentoPct', namespaces=nsp).text) if detalle.find('ns:DescuentoPct', namespaces=nsp) is not None else 0.0
        desc_monto = float(detalle.find('ns:DescuentoMonto', namespaces=nsp).text) if detalle.find('ns:DescuentoMonto', namespaces=nsp) is not None else 0.0
        monto_item = float(detalle.find('ns:MontoItem', namespaces=nsp).text) if detalle.find('ns:MontoItem', namespaces=nsp) is not None else 0.0
        
        # Agregar los datos una lista de dict
        data.append({
            'Nro_Linea': NroLin,
            'Rut_Prov':RUT,
            'Proveedor': nombre_proveedor,
            'Factura':Folio,
            'Fecha': FechaEmis,
            'Codigo' : SKU,
            'Detalle' : nombre_prod,
            'Cantidad' : cantidad,
            'Precio' : precio,
            'Desc_Porc' : descuento,
            'Desc_Monto' : desc_monto,
            'Monto_Item' : monto_item
        })

    DescRecargo = []
    #reviso si tiene descuento o recargo globales, si no lo encuentra, le podrá un string "X"
    for x in documento.findall('ns:DscRcgGlobal', namespaces=nsp):
        tipo = x.find('ns:TpoMov', namespaces=nsp).text if x.find('ns:TpoMov', namespaces=nsp) is not None else 'N/A'
        GlosaDR = x.find('ns:GlosaDR', namespaces=nsp).text if x.find('ns:GlosaDR', namespaces=nsp) is not None else 'N/A'
        ValorDR = float(x.find('ns:ValorDR', namespaces=nsp).text) if x.find('ns:ValorDR', namespaces=nsp) is not None else 0.0
        DescRecargo.append({
            'Rut_Prov':RUT,
            'Tipo Desc/Rec': tipo, 
            'Glosa Desc/Rec': GlosaDR,
            'Valor Desc/Rec': ValorDR
        })
        
    DocRef = []    
    for y in documento.findall('ns:Referencia', namespaces=nsp):
        TpoDocRef = int(y.find('ns:TpoDocRef', namespaces=nsp).text) if y.find('ns:TpoDocRef', namespaces=nsp) is not None else 0
        FolioRef = int(y.find('ns:FolioRef', namespaces=nsp).text) if y.find('ns:FolioRef', namespaces=nsp) is not None else 0
        FchRef = y.find('ns:FchRef', namespaces=nsp).text if y.find('ns:FchRef', namespaces=nsp) is not None else '1900-01-01'
        FchRef = Calcular_fecha(False, FchRef)
        DocRef.append({
            'Rut_Prov':RUT,
            'Tipo Doc Ref': TpoDocRef,
            'Folio Ref': FolioRef,
            'Fecha Ref': FchRef
        })
    
    df = pd.DataFrame(data)
    # Aquí valido si son vacios o nos datos de Doc. Referencias y Descuentos y Recargos. 
    if bool(DescRecargo):
        df_DR = pd.DataFrame(DescRecargo)
    else:
        df_DR = pd.DataFrame()
    
    if bool(DocRef):
        df_R = pd.DataFrame(DocRef)
    else:
        df_R = pd.DataFrame()
        
    return df, df_DR, df_R, nombre_proveedor

def Calcular_fecha(conHora, Fch=None):
    
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

def Nombrar_archivo(proveedor:str,tipo):
    fecha = Calcular_fecha(True)
    if tipo == "Detalle":
        ruta_excel = fecha + '_Detalle_Productos_' + proveedor.title() + '.xlsx'
    elif tipo == "DescRec":
        ruta_excel = fecha + '_Desc_Rec_' + proveedor.title() + '.xlsx'
    elif tipo == "Ref":
        ruta_excel = fecha + '_Referencia_' + proveedor.title() + '.xlsx'
    return ruta_excel

def Exportar_df_excel(df, tipo, proveedor:str):
    ruta_excel = Nombrar_archivo(proveedor,tipo)
    # Exportar el DataFrame a Excel
    df.to_excel(ruta_excel, index=False)
    print(f"Archivo Excel creado exitosamente en {ruta_excel}")

def Entregar_DataFrames_DTE(ruta_xml):
    df, df_DR, df_R, proveedor = Cargar_datos_XML(ruta_xml)
    
    Exportar_df_excel(df,"Detalle", proveedor)
    
    if not df_DR.empty:
        Exportar_df_excel(df_DR,"DescRec", proveedor)
    
    if not df_R.empty:
        Exportar_df_excel(df_R,"Ref", proveedor)
        


if __name__ == "__main__":
    # Cargo y parseo el archivo xml
    ruta_xml = "Factura.xml"
    df, df_DR, df_R, proveedor = Cargar_datos_XML(ruta_xml)
    
    Exportar_df_excel(df,"Detalle", proveedor)
    
    if not df_DR.empty:
        Exportar_df_excel(df_DR,"DescRec", proveedor)
    if not df_R.empty:
        Exportar_df_excel(df_R,"Ref", proveedor)
    
