# and, or, not

gas = True
encendido =  True
edad = 18

if gas and encendido:
    print("Puedes avanzar")

"""
and valida todas las operaciones y si todas son verdaderas da como resultado True
or si alguna de las operaciones es verdadera da True y solo en caso que todas sean falsas dara False
not funciona como negacion, si el resultado es True arroja False y viceversa
"""

if not gas or encendido or edad > 17:
    print("Puedes Avanzar")