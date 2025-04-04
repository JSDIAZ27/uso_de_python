#caso de uso el login a una aplicacion 
#usuario = input("por favor ingrese su usuario")
#password = input("por favor ingrese su password")

#if usuario =="andres" and password=="1234":
#    print("usuario puede ingresar")

    #ejemplo 2
dia=input("ingrese el dia de la semana")
match dia:
    case "sabado" | "domingo":
        print(f"{dia} es fin de semana")
    case"lunes":
        print(f"{dia} es el dia mas dificil")
    case"martes" | "miercoles" | "jueves":
        print("es un dia normal")
    case _:
        print("el texto no es un dia de la semana")
        




    