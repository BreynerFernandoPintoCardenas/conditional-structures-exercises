numeroONe=int(input("Enter a number"))
numeroTwo=int(input("Enter a number"))
numeroThre=int(input("Enter a number"))


if numeroONe<numeroTwo<numeroThre: #uno, dos, tres
    print(f"""
       
        {numeroONe, numeroTwo, numeroThre}
""")
elif numeroTwo<numeroONe<numeroThre: #dos, uno, tres     
    print(f"""       
        {numeroTwo, numeroONe, numeroThre}
""")
elif numeroONe<numeroThre<numeroTwo: #uno, tres, dos
    print(f"""       
        {numeroONe,numeroThre, numeroTwo}
""")
elif numeroThre<numeroONe<numeroTwo: #tres, uno, dos
    print(f"""       
        {numeroThre,numeroONe, numeroTwo}
""")
elif numeroTwo<numeroThre<numeroONe: #two, tres, one
    print(f"""       
        {numeroTwo,numeroThre, numeroONe}
""")
elif numeroThre<numeroTwo<numeroONe: #tres, dos, uno
    print(f"""       
        {numeroThre,numeroTwo, numeroONe}
""")    