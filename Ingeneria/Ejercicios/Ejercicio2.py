import  returnArreglo as ra, returnPromedio as rp, returnAbajo as rba
n = int(input("Ingrese la cantidad de numeros que desea ingresar: "))
arreglo = ra.returArreglo(n)
print("El arreglo ingresado es:", arreglo)

promedio = sum(arreglo)/n
print("El promedio de los numeros ingresados es:", promedio)

abajo = rba.returnAbajo(arreglo)
print("Los numeros por debajo del promedio son:", abajo)