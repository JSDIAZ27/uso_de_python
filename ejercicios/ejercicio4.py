'''
Problema: Escribe un programa que determine si un número ingresado por el 
usuario es par o impar utilizando el operador módulo %.
'''
# Solicitar un número al usuario
numero = int(input("Ingrese un número: "))

# Verificar si es par o impar
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
