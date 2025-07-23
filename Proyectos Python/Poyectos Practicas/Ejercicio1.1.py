# Promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curoso = 1.5

# Duracion de Crudos
crudo_promedio = 5
crudo_dalto = 3.5

# Diferencia de Cursos
diferencia_con_min = 100 - dalto_curoso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curoso * 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - dalto_curoso / otros_cursos_promedio * 100

# Calculando el porcentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curoso * 1000 // crudo_dalto / 10

print(f'El curso de Dalto dura un {diferencia_con_min}% menos que el mas rapido')
print(f'El curso de Dalto dura un {diferencia_con_max}% menos que el mas lento')
print(f'El curso de Dalto dura un {diferencia_con_promedio}% menos que el mas rapido')

# Mostrando la cantidad de espacion vacios que se remueven 
print(f'El curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio')

# Mostrando diferencias si los cursos duraran 10 horas
print(f'Ver 10 horas de esta curso equivale a ver {otros_cursos_promedio * 100 // dalto_curoso / 10} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {dalto_curoso * 1000 // otros_cursos_promedio / 10} horas de este cursos')