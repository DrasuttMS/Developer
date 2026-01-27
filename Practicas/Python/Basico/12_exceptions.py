## Exception ##

## Manejo de excepciones en Python, son el manejo de errores en tiempo de ejecución ##

number_one = 5
number_two = 10
number_two = "5"


try:
    print(number_one + number_two) 
    print("La suma se ha realizado correctamente")
except:
    print("Se ha producido un error al intentar sumar los valores")

#try except else
try:
    print(number_one + number_two) 
    print("La suma se ha realizado correctamente")
except:
    print("Se ha producido un error al intentar sumar los valores")
else:
    print("La ejecución del bloque try ha sido exitosa")

#try except else finally
try:
    print(number_one + number_two) 
    print("La suma se ha realizado correctamente")
except:
    print("Se ha producido un error al intentar sumar los valores")
else:
    print("La ejecución del bloque try ha sido exitosa")
finally:
    print("La ejecución del bloque finally se ejecuta siempre")

#try except por tipo de excepción
try:
    print(number_one + number_two) 
    print("La suma se ha realizado correctamente")
except TypeError:
    print("Se ha producido un error al intentar sumar los valores")