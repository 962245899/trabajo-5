#INPUT
print("BOTICA SIEMPRE BIEN")
cliente=input("Ingrese el nombre del cliente:")
vendedor=input("ingrese el nombre del vendedor:")
nº_de_jarabe=int(input("Ingrese Nº de jarabe:"))
nº_de_pastillas=int(input("ingrese el nº_de_pastillas"))
precio_unitario_jarabe=float(input("Ingrese precio unitario_jarabe:"))
precio_unitario_pastillas=float(input("ingrese precio unitario_pastillas"))

# PROCESSING
total = ((precio_unitario_jarabe * nº_de_jarabe)+(precio_unitario_pastillas * nº_de_pastillas))

#verificador
limite=(total>100)

# OUTPUT
print("#######################")
print("#BOTICA SIEMPRE BIEN#")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Item   :  ",nº_de_pastillas,"  nº_de_pastillas")
print("# Precio Unitario_pastillas  :  S/.", precio_unitario_pastillas)
print("# Item   :  ",nº_de_jarabe,"  nº_de_jarabe")
print("# Precio Unitario_jarabe   :  S/.", precio_unitario_jarabe)
print("# Total  :  S/.", total)
print("# nombre del vendedor:", vendedor)
print("#######################")
print("el total es menor que el limite?", limite)
