# Solicitar la entrada de cuatro números
numero1 = int(input("Ingrese número: "))
numero2 = int(input("Ingrese número: "))
numero3 = int(input("Ingrese número: "))
numero4 = int(input("Ingrese número: "))

# Crear una lista con los números
numeros = [numero1, numero2, numero3, numero4]

# Ordenar la lista
numeros.sort()

# Mostrar los números en orden
print(" ".join(map(str, numeros)))
