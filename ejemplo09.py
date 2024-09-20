# 9.- Escribir un programa que pregunte al usuario una cantidad a invertir,
# el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

cantidadInvertir = int(input("Ingrese cantidad a invertir: "))
interesAnual = float(input("ingrese interes anual: "))
numeroAños = int(input("Ingrese cantidad de años: "))

capitalObtenido = round((cantidadInvertir * (1 + interesAnual) ** numeroAños), 2)
print("El capital obtenido es: ", (str(capitalObtenido)))
#print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))