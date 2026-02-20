buscar = 10

for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Encontrado", buscar)
        break
else:
    print("No encontrado el numero")
    
for char in "Ultimate Python":
    print(char)