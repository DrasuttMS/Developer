## Diccionaries ##

my_dict = dict()
my_other_dict = {}

my_other_dict = {"Nombre": "Max", "Apellido": "Salas", "Edad": 32, "Ciudad": "Santiago", 1:"Python"}
print(my_other_dict)

my_dict = {
    "Nombre": "Max",
    "Apellido": "Salas",
    "Edad": 32,
    "Ciudad": "Santiago",
    1:"Python",
    "Lenguajes": {"Python", "JavaScript", "CSharp"}
    }

print(my_dict)

my_dict["Nombre"] = "Miguel"
print(my_dict["Nombre"])