#INPUT
print("DONOFRIO")
cliente=input("Ingrese el nombre del cliente:")
vendedor=input("ingrese el nombre del vendedor:")
nº_de_panetones=int(input("Ingrese Nº de panetones:"))
nº_de_helados=int(input("ingrese el nº_de_helados"))
precio_unitario_panetones=float(input("Ingrese precio unitario_panetones:"))
precio_unitario_heladoss=float(input("ingrese precio unitario_helados"))

# PROCESSING
total = ((precio_unitario_heladoss* nº_de_helados)+(precio_unitario_panetones * nº_de_panetones))

#verificador
limite=(total>500)

# OUTPUT
print("#######################")
print("#DONOFRIO#")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Item   :  ",nº_de_panetones,"  nº_de_panetones")
print("# Precio Unitario_panetones  :  S/.", precio_unitario_panetones)
print("# Item   :  ",nº_de_helados,"  nº_de_helados")
print("# Precio Unitario_helados   :  S/.", precio_unitario_helados)
print("# Total  :  S/.", total)
print("# nombre del vendedor:", vendedor)
print("#######################")
print("el total es menor que el limite?", limite)
