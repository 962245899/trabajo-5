#INPUT
cliente=input("Ingrese el nombre del cliente:")
vendedor=input("ingrese el nombre del vendedor:")
kg=int(input("Ingrese Nr Kg de carne:"))
precio_unitario=float(input("Ingrese precio unitario:"))

# PROCESSING
total = (precio_unitario * kg)

#verificador
limite=(total<500)

# OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Item   :  ",kg,"  kg carne")
print("# Precio Unitario   :  S/.", precio_unitario)
print("# Total  :  S/.", total)
print("# nombre del vendedor:", vendedor)
print("#######################")
print("el total es menor que el limite?", limite)
