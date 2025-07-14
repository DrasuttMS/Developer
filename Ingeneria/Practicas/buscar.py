miLista = [2,12,5,1,7,8,2,9,0,4,2,13,26,6]
num = int(input("Ingrese un numero --> "))

if(num in miLista):
    i = 0
    while(num!=miLista[i]):
        i = i + 1
    print("El elemento",num," Esta en el indice",i)
else:
    print("Numero no existe en la lista")
