# 7.- Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
#  calcule el índice de masa corporal y lo almacene en una variable,
#  y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc>
#  es el índice de masa corporal calculado redondeado con dos decimales.
kg = float(input("Ingresa tu peso: "))
estatura = float(input("Ingrese su estatura: "))
I = round((kg/(estatura)**2),2)
print("Su IMC es: ", I)

#print("Tu indice de masa corportal es " + str(I))

