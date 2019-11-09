#INPUT
print("ASERRADERO TU BUENA TABLA")
cliente=input("Ingrese el nombre del cliente:")
vendedor=input("ingrese el nombre del vendedor:")
nº_de_tablas=int(input("Ingrese Nº de tablas:"))
precio_unitario=float(input("Ingrese precio unitario:"))

# PROCESSING
total = (precio_unitario * nº_de_tablas)

#verificador
limite=(total>1000)

# OUTPUT
print("#######################")
print("#ASERRADERO TU BUENA TABLA#")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Item   :  ",nº_de_tablas,"  nº_de_tablas")
print("# Precio Unitario   :  S/.", precio_unitario)
print("# Total  :  S/.", total)
print("# nombre del vendedor:", vendedor)
print("#######################")
print("el total es menor que el limite?", limite)
