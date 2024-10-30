# Función para determinar el estado del set
def estado_set(juegos_a, juegos_b):
    # Verificar si el resultado es inválido
    if (juegos_a >= 7 and juegos_b >= 6) or (juegos_b >= 7 and juegos_a >= 6):
        print("Invalido")
        return

    # Comprobar si A ha ganado
    if juegos_a >= 6 and juegos_a - juegos_b >= 2:
        print("Gano A")
    # Comprobar si B ha ganado
    elif juegos_b >= 6 and juegos_b - juegos_a >= 2:
        print("Gano B")
    # Si el set está empatado a 5 juegos
    elif juegos_a == 5 and juegos_b == 5:
        print("Aun no termina")
    # Si el set está empatado a 6 juegos
    elif juegos_a == 6 and juegos_b == 6:
        print("Aun no termina")
    # Si el set aún no ha terminado
    elif juegos_a < 6 and juegos_b < 6:
        print("Aun no termina")
    else:
        print("Invalido")

# Solicitar juegos ganados por A y B
juegos_a = int(input("Juegos ganados por A: "))
juegos_b = int(input("Juegos ganados por B: "))

# Llamar a la función para determinar el estado del set
estado_set(juegos_a, juegos_b)

