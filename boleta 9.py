#INPUT
print("ALICORP")
cliente=input("Ingrese el nombre del cliente:")
vendedor=input("ingrese el nombre del vendedor:")
nº_de_galletas=int(input("Ingrese Nº de galletas:"))
nº_de_caramelos=int(input("ingrese el nº_de_caramelos"))
precio_unitario_galletas=float(input("Ingrese precio unitario_galletas:"))
precio_unitario_caramelos=float(input("ingrese precio unitario_caramelos"))

# PROCESSING
total = ((precio_unitario_caramelos* nº_de_caramelos)+(precio_unitario_galletas * nº_de_galletas))

#verificador
limite=(total>100)

# OUTPUT
print("#######################")
print("#ALICORP#")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Item   :  ",nº_de_caramelos,"  nº_de_caramelos")
print("# Precio Unitario_caramelos  :  S/.", precio_unitario_caramelos)
print("# Item   :  ",nº_de_galletas,"  nº_de_galletas")
print("# Precio Unitario_galletas   :  S/.", precio_unitario_galletas)
print("# Total  :  S/.", total)
print("# nombre del vendedor:", vendedor)
print("#######################")
print("el total es menor que el limite?", limite)
