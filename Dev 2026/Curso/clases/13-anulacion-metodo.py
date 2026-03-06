class Ave:
    def __init__(self):
        self.volador = "Volador"
        
    def vuela(self):
        print("vuela ave")

class Pato(Ave):
    def __init__(self):
        super().__init__()
        self.nada = "Nadador"
        
pato = Pato()
pato.vuela()
print(pato.volador, pato.nada)