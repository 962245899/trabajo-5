#INPUT
print("LA TABERNA")
cliente=input("Ingrese el nombre del cliente:")
vendedor=input("ingrese el nombre del vendedor:")
nº_de_vinos=int(input("Ingrese Nº de vinos:"))
nº_de_pisco=int(input("ingrese el nº_de_pisco"))
precio_unitario_vinos=float(input("Ingrese precio unitario_vinos:"))
precio_unitario_pisco=float(input("ingrese precio unitario_pisco"))

# PROCESSING
total = ((precio_unitario_pisco* nº_de_pisco)+(precio_unitario_vinos * nº_de_vinos))

#verificador
limite=(total>500)

# OUTPUT
print("#######################")
print("#LA TABERNA#")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Item   :  ",nº_de_vinos,"  nº_de_vinos")
print("# Precio Unitario_vinos  :  S/.", precio_unitario_vinos)
print("# Item   :  ",nº_de_pisco,"  nº_de_pisco")
print("# Precio Unitario_pisco   :  S/.", precio_unitario_pisco)
print("# Total  :  S/.", total)
print("# nombre del vendedor:", vendedor)
print("#######################")
print("el total es menor que el limite?", limite)
