def promedio(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    resultado /= len(numeros)
    print(resultado)

promedio(1,2,3,4,5)