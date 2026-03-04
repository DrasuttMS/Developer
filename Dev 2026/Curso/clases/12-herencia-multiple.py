class Animal:
    def comer(self):
        print("comiendo")

class Perro(Animal):
    def pasear(self):
        print("pasenado")
    
class Chanchito(Perro, Animal):
    def programar(self):
        print("programando")

chanchito = Chanchito()
chanchito.pasear()