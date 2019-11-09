#INPUT
print("CLARO")
cliente=input("Ingrese el nombre del cliente:")
vendedor=input("ingrese el nombre del vendedor:")
nº_de_celulares=int(input("Ingrese Nº de celulares:"))
nº_de_accesorios=int(input("ingrese el nº_de_accesorios"))
precio_unitario_celulares=float(input("Ingrese precio unitario_celulares:"))
precio_unitario_accesorios=float(input("ingrese precio unitario_accesorios"))

# PROCESSING
total = ((precio_unitario_celulares* nº_de_celulares)+(precio_unitario_accesorios * nº_de_accesorios))

#verificador
limite=(total>1000)

# OUTPUT
print("#######################")
print("#CLARO#")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Item   :  ",nº_de_celulares,"  nº_de_celulares")
print("# Precio Unitario_celulares  :  S/.", precio_unitario_celulares)
print("# Item   :  ",nº_de_accesorios,"  nº_de_accesorios")
print("# Precio Unitario_accesorios   :  S/.", precio_unitario_accesorios)
print("# Total  :  S/.", total)
print("# nombre del vendedor:", vendedor)
print("#######################")
print("el total es menor que el limite?", limite)
