#INPUT
print("TOYOTA")
cliente=input("Ingrese el nombre del cliente:")
vendedor=input("ingrese el nombre del vendedor:")
nº_de_autos=int(input("Ingrese Nº de autos:"))
nº_de_camionetas=int(input("ingrese el nº_de_camionetas"))
precio_unitario_autos=float(input("Ingrese precio unitario_autos:"))
precio_unitario_camionetas=float(input("ingrese precio unitario_camionetas"))

# PROCESSING
total = ((precio_unitario_camionetas* nº_de_camionetas)+(precio_unitario_autos * nº_de_autos))

#verificador
limite=(total>10000)

# OUTPUT
print("#######################")
print("#TOYOTA#")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Item   :  ",nº_de_autos,"  nº_de_autos")
print("# Precio Unitario_autos  :  S/.", precio_unitario_autos)
print("# Item   :  ",nº_de_camionetas,"  nº_de_camionetas")
print("# Precio Unitario_camionetas   :  S/.", precio_unitario_camionetas)
print("# Total  :  S/.", total)
print("# nombre del vendedor:", vendedor)
print("#######################")
print("el total es menor que el limite?", limite)
