# Función para determinar el tipo de triángulo
def tipo_triangulo(a, b, c):
    # Verificar si es un triángulo válido
    if a + b > c and a + c > b and b + c > a:
        # Determinar el tipo de triángulo
        if a == b == c:
            return "El triángulo es equilátero."
        elif a == b or a == c or b == c:
            return "El triángulo es isósceles."
        else:
            return "El triángulo es escaleno."
    else:
        return "No es un triángulo válido."

# Solicitar los lados del triángulo
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

# Llamar a la función y mostrar el resultado
resultado = tipo_triangulo(a, b, c)
print(resultado)
