numero = 1

while numero < 100:
    print(numero)
    numero *= 2
    
"""
Primero evalua la condicion proporcionada y luego ejecuta el codigo, si no aplica 
"""

comando = ""

while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)
    
