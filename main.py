# Solicita al usuario que ingrese un año
año = int(input("Pon tu año y yo te diré si es bisiesto: "))

# Verifica si el año es divisible por 100
divisible100 = (año % 100) == 0

# Comienza a verificar si el año es bisiesto
if (año % 4) == 0:
    # Si el año es divisible por 100, se debe verificar si es también divisible por 400
    if divisible100:
        if (año % 400) == 0:
            print(f"{año} es bisiesto")
        else:
            print(f"{año} no es bisiesto")
    else:
        print(f"{año} es bisiesto")
else:
    print(f"{año} no es bisiesto")
