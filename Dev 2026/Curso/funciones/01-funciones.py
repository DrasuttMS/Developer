def hola(nombre, apellido):
    print("Hola Mundo")
    print(f"Ultimate Python {nombre} {apellido}")


hola("Max", "Salas")

#Funciones con parametros opcionales
def hi(nombre, apellido="felix"):
    print("Hola Mundo")
    print(f"Ultimate Python {nombre} {apellido}")

hi("Max")

#ingreso de funciones segun lo que ingreso, de ser asi, tengo que nombrar todos los argumentos  
hola(apellido ="Salas", nombre= "Max")
