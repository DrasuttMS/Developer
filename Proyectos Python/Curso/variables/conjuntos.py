# creando un conjunto con set

conjunto = set(["Max", "Ines", "Luna", "Anto",("dato en lista")])

# metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(("dato 1","dato 2"))
conjunto2 = {conjunto1, "dato 3", "dato 4"}

print(conjunto2)

conj1 = {1,3,5,7,9}
conj2 = {1,3,9}
resultado = conj2.issubset(conj1)
print(resultado)
# Verificando si conj2 es un subconjunto de conj1   

# frozenset: es un conjunto inmutable
conj3 = frozenset([1,2,3,4,5])

# issubset: verifica si un conjunto es un subconjunto de otro
print(conj3.issubset({1,2,3,4,5,6,7,8,9,10}))

# isdisjoint: verifica si dos conjuntos no tienen elementos en común
conj4 = {1,2,3} 

# dict() crea un diccionario a partir de un iterable de pares clave-valor
conj5 = {4,5,6}

# fromkeys: crea un diccionario a partir de un iterable, usando los elementos como claves y un valor predeterminado
diccionario = dict.fromkeys(conj5, "valor predeterminado")
print(diccionario)
