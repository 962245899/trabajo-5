#INPUT
print("GLOBAL VISION")
cliente=input("Ingrese el nombre del cliente:")
vendedor=input("ingrese el nombre del vendedor:")
nº_de_mouse=int(input("Ingrese Nº de mouse:"))
nº_de_laptop=int(input("ingrese el nº_de_laptop"))
precio_unitario_mouse=float(input("Ingrese precio unitario_mouse:"))
precio_unitario_laptop=float(input("ingrese precio unitario_laptop"))

# PROCESSING
total = ((precio_unitario_mouse * nº_de_mouse)+(precio_unitario_laptop * nº_de_laptop))

#verificador
limite=(total>3000)

# OUTPUT
print("#######################")
print("#GLOBAL VISION#")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Item   :  ",nº_de_mouse,"  nº_de_mouse")
print("# Precio Unitario_mouse   :  S/.", precio_unitario_mouse)
print("# Item   :  ",nº_de_laptop,"  nº_de_laptop")
print("# Precio Unitario_laptop   :  S/.", precio_unitario_laptop)
print("# Total  :  S/.", total)
print("# nombre del vendedor:", vendedor)
print("#######################")
print("el total es menor que el limite?", limite)
