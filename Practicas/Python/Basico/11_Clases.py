## Clases ##
## Los nombres de las clases en Python se escriben en CamelCase ##

class MyPerson:
    pass 

print(MyPerson())

class Person:
    # Método constructor
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"

    def walk(self):
        print(f"{self.full_name} está caminando")

my_person = Person("Max", "Salas")
print("El nombre completo de la persona es:", my_person.full_name)
my_person.walk()
