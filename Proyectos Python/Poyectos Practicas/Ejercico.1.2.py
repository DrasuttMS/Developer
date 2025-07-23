frase = input("Dime alguna frase y calculo cuanto tiempo te lleva decirla: ")
cantidad_separadas = frase.split(" ")
cantidad_de_palabras = len(cantidad_separadas)
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirla')  # Asumiendo 2 segundos por palabra 
print(f'Dalto lo diria en {cantidad_de_palabras *100 //2 * 1.3 /100} segundos')  # Asumiendo que Dalto habla un 30% más rápido  
