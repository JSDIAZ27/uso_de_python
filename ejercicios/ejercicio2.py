'''
Problema: Escribe un programa que verifique si una palabra ingresada por el usuario está 
en la siguiente frase:
"Python es un lenguaje de programación poderoso".
'''
 # Frase predeterminada
frase = "Python es un lenguaje de programación poderoso"

# Solicitar palabra al usuario
palabra = input("Ingrese una palabra: ")

# Verificar si la palabra está en la frase (El operador in en Python se utiliza para 
# verificar si un elemento está contenido en una secuencia como cadenas de 
# texto, listas, tuplas, conjuntos o diccionarios.
# Es muy versátil y uno de los operadores más usados.)
if palabra in frase:
    print(f"La palabra '{palabra}' está en la frase.")
else:
    print(f"La palabra '{palabra}' no está en la frase.")
