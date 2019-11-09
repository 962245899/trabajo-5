#INPUT
print("GRUPO GLORIA")
cliente=input("Ingrese el nombre del cliente:")
vendedor=input("ingrese el nombre del vendedor:")
nº_de_leche=int(input("Ingrese Nº de leche:"))
nº_de_frugos=int(input("ingrese el nº_de_frugos"))
precio_unitario_leche=float(input("Ingrese precio unitario_leche:"))
precio_unitario_frugos=float(input("ingrese precio unitario_frugos"))

# PROCESSING
total = ((precio_unitario_leche* nº_de_leche)+(precio_unitario_frugos * nº_de_frugos))

#verificador
limite=(total>50)

# OUTPUT
print("#######################")
print("#GRUPO GLORIA#")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Item   :  ",nº_de_frugos,"  nº_de_frugos")
print("# Precio Unitario_frugos  :  S/.", precio_unitario_frugos)
print("# Item   :  ",nº_de_leche,"  nº_de_leche")
print("# Precio Unitario_leche   :  S/.", precio_unitario_leche)
print("# Total  :  S/.", total)
print("# nombre del vendedor:", vendedor)
print("#######################")
print("el total es menor que el limite?", limite)
