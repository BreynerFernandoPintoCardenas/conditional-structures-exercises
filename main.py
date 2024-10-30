# Solicitar el primer operando
operando1 = float(input("Operando: "))

# Solicitar el operador
operador = input("Operador: ")

# Solicitar el segundo operando
operando2 = float(input("Operando: "))

# Realizar la operación según el operador
if operador == '+':
    resultado = operando1 + operando2
    print(f"{operando1} + {operando2} = {resultado}")
elif operador == '-':
    resultado = operando1 - operando2
    print(f"{operando1} - {operando2} = {resultado}")
elif operador == '*':
    resultado = operando1 * operando2
    print(f"{operando1} * {operando2} = {resultado}")
elif operador == '/':
    if operando2 != 0:  # Comprobar si el divisor no es cero
        resultado = operando1 / operando2
        print(f"{operando1} / {operando2} = {resultado}")
    else:
        print("Error: División por cero no está permitida.")
elif operador == '**':
    resultado = operando1 ** operando2
    print(f"{operando1} ** {operando2} = {resultado}")
else:
    print("Error: Operador no válido.")
