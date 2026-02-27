# De esta forma, anteponiendo el simbolo * antes del nombre del parametro me permitara iterar en todos

def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(2, 5, 7,6,7,4,8,4,3)
