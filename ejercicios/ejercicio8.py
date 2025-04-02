'''Problema: Solicitar al usuario dos conjuntos de números y luego mostrar:

    La unión de ambos conjuntos.

    La intersección de ambos conjuntos'''
    
#solucion 
#entrada1="8 9" #imput("ingrese los numeros del primer conjunto")
#print(map(int, entrada1))#8 9 ---> en un recorrido de una lista-es un mapeo y lo esta pasando a enteros 
#print(map(int, entrada1.split()))# 8,9
#print(set(map(int, entrada1.split())))# {8,9}


# Pedir los conjuntos al usuario
conjunto1 = set(map(int, input("Ingrese los números del primer conjunto separados por espacio: ").split()))
conjunto2 = set(map(int, input("Ingrese los números del segundo conjunto separados por espacio: ").split()))
union=conjunto1 | conjunto2
interseccion= conjunto1.intersection(conjunto2)
print(conjunto1, conjunto2, union, interseccion)
