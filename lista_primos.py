"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Declaraciones
divisores = []
# Entradas
entrada = int(input("Introduzca un número: "))

# Proceso
divisor = 2
for numero in range (1, entrada + 1):
    while divisor < entrada:
        if entrada % divisor == 0 and divisor != entrada:
            break
        divisor += 1
    else:
        divisores.append(divisor)
        print(f"Los números primos menores o igaules a {entrada} son: {divisores}")


        

