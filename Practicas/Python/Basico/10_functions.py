## Functions ##

def my_function():
    print("Hola desde mi función")

my_function()

def sum_two_numbers(first_number, second_number):
    print(first_number + second_number)

sum_two_numbers(5, 7)

def sum_two_numbers_with_return(first_number, second_number):
    return first_number + second_number

result = sum_two_numbers_with_return(10, 15)
print("El resultado de la suma es:", result)

def print_name(name = "Sin nombre", surname = "Sin apellido"):
    print("Tu nombre es:", name, "y tu apellido es:", surname)

print_name("Juan", "Pérez")
print_name()  # Usando los valores por defecto

def print_texts(*texts):
    for text in texts:
        print("Texto:", text)

print_texts("Hola", "Mundo", "Desde", "Funciones", "Max Salas")

def print_text(*texts):
    print(*texts)

print_text("Hola", "Mundo", "Desde", "Funciones", "Max Salas")