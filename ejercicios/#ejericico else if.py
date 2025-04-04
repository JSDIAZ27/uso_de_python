#ejericico 1
"solictiar una edad y clasificarla"
"en menores de esdad (0 - 17), adultos (18 - 64) y"
"adultos mayores de (65+)"
"para este ejercicio usar if elif else "
"y tambien usar match/case"
""

#solucion 

edad=int(input("ingrese su edad:"))
if 0<= edad <= 17:
    print("eres menor de edad")
elif 18<= edad <= 64:
    print("eres un adulto")
elif edad >= 65:
    print("eres un adulto mayor")
else:
    print("la edad no es valida")
    
