numberOne=int(input("Enter one number "))
numberTwo=int(input("Enter second number "))

cociente=numberOne//numberTwo
resto=numberOne%numberTwo

if resto==0: 
    print("la divison es exacta")
    print(f"""
    cociente: {cociente}
    resto: {resto}
""")

else:
    print(f"""
    la division no es exacta.
    cociente: {cociente}
    resto: {resto}
""")