## Loops ##

## While Loop ##

my_condition = 0

while my_condition < 10:
    print("Mi condición es menor que 10")
    my_condition += 1  # Incrementa el valor de my_condition en 1
    print("Valor de my_condition:", my_condition)
    if my_condition == 6:
        print("Se detiene la ejecución del loop")
        break
else:
    print("Mi condición es mayor o igual que 10")

## Bucle For ##

my_list = [35, 24, 62, 52, 12, 98, 75]

for element in my_list:
    print("Elemento de la lista:", element)
    if element == 24:
        print("Se detiene la ejecución del bucle for")
        break
else:
    print("El bucle for ha finalizado correctamente")

for i in range(6):
    print("Número de la iteración:", i)
    if i == 3:
        print("Se salta la iteración número 3")
        continue
    print("Continuando con la siguiente instrucción...")