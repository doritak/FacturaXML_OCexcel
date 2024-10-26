# Parsear una Factura XML y Ordenarlo con la Orden de Compra en Excel
## Objetivo:
Poder revisar y comparar las facturas electrónicas con las órdenes de compra **OC** que están en Excel en la empresa. 
Las facturas electrónicas **DTE** tienen un formato pre-establecido en XML, y contiene toda la información de compra, y a veces puede obtener el número de la orden de compra en documento de referencia código 801, como también un folio de guía de despacho con el documento de referencia código 56.

Las órdenes de compra **OC** estan Excel, y se podría parsear el detalle porque comienza con una celda de nombre "Código" que representa al código del producto. 

La idea es poder obtener en un dataframe el detalle del DTE y por otra parte el detalle del OC para luego construir un nuevo dataframe con la comparación de precios, cantidades, montos totales por producto. 

Entregándole a usuario un forma automatizada de comparación, para que éste sólo evalué los casos problemáticos, como no se encuentra el producto, o cambios de códigos de productos, cambio de cantidades o precios entre otros. 

## Parsear un archivo XML
Para esto usamos el `import xml.etree.ElementTree as ET` y luego llamamos al XML. 
```
with open(ruta_xml, encoding='ISO-8859-1') as file:
  tree = ET.parse(file)
  root = tree.getroot()
```
[!IMPORTANT] Se debe definir el namespace que se indica en el formato del XML del SII. Porque sino, no puedes encontrar la rama del Document
```
# Definir el espacio de nombres
nsp  = {'ns': 'http://www.sii.cl/SiiDte'}
```
