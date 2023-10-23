"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Declaraciones
numeros = []

# Entradas
entrada = int(input("Introduzca un número: "))

# Proceso
for numero in range (2, entrada + 1):
    resultado = 0
    for divisor in range(2, numero):
        if numero % divisor == 0:
            break
        else:
            numeros.append(numero)
            print(f"Los números primos menores o iguales a {entrada} son: {numeros}")


        

