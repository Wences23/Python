ingreso = int(input("ingrese su salario:   "))
gastoMensual = float(input("ingrese sus gastos mensuales:  "))

if ingreso >= 10000:
    if ingreso - gastoMensual < 0:
        print("estas en deficit")      
    elif ingreso - gastoMensual >= 3000:
        print("buena capacidad de ahorro")
    else:
        print("estas gastando mucho")
    
elif ingreso >= 1000:
    if ingreso - gastoMensual < 0:
        print("estas en deficit")      
    elif ingreso - gastoMensual >= 100:
        print("no vas a viajar nunca a este ritmo")
    else:
        print("estas gastando mucho")

elif ingreso >= 200:
    if ingreso - gastoMensual < 0:
        print("estas en deficit")      
    elif ingreso - gastoMensual >= 50:
        print("no vas a viajar nunca a este ritmo, ahorra mas que te tenes que ir de venezuela")
    else:
        print("estas gastando mucho")

else:
    print("sos pobre")