"""
1. Continuando con el ejercicio del video pedir tu nombre y tu año de
    nacimiento. Mostrar por consola cuanto años tenes.

    Ingrese su nombre: Eric
    Ingrese su año de nacimiento: 1991
    
    "Hola Eric de 28 años"

    Más adelante veremos como solucionar el problema de si todavia no pasó tu
    mes de cumpleaños
"""

nombre = input("Ingrese su nombre: ")
nacimiento = int(input("Ingrese su año de nacimiento: ")) 
edad = 2019 - nacimiento

print(f"Hola {nombre} de {edad} años")

"""
2. Pedir 2 numeros por consola y realizar las 4 operaciones básicas.
    Suma, resta, multiplicación y división. Mostrar los resultados por consola

    Ingrese el primer numero: 6
    Ingrese el segundo numero: 2

    "Suma: 8"
    "Resta: 4"
    "Multiplicación: 12"
    "División: 3"

    Más adelante veremos como resolver el problema cuando se divide por 0
"""

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
