# Función para calcular el IMC y determinar el riesgo
def condicion_riesgo(estatura, peso, edad):
    # Calcular el IMC
    imc = peso / (estatura ** 2)

    # Determinar la condición de riesgo
    if edad < 45:
        if imc < 22.0:
            return "Riesgo bajo"
        else:
            return "Riesgo medio"
    else:  # edad >= 45
        if imc < 22.0:
            return "Riesgo medio"
        else:
            return "Riesgo alto"

# Solicitar datos al usuario
estatura = float(input("Ingrese su estatura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
edad = int(input("Ingrese su edad: "))

# Obtener y mostrar la condición de riesgo
riesgo = condicion_riesgo(estatura, peso, edad)
print(f"Su condición de riesgo es: {riesgo}")

