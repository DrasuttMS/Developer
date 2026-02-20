primer_nombre = input("Ingresa tu primer nombre: ")
segundo_nombre = input("Ingresa tu segundo nombre: ")
apellido_paterno = input("Ingresa apellido paterno: ")
apellido_materno = input("Ingresa apellifo materno: ")

mensaje = f"""
El nombre completo ingresado es: {primer_nombre} {segundo_nombre} {apellido_paterno} {apellido_materno}
"""

print(primer_nombre.strip().capitalize(), segundo_nombre.strip().capitalize(),apellido_paterno.strip().capitalize(), apellido_materno.strip().capitalize()) 