tweet = input("Ingrese un tweet: ")

if len(tweet) > 20:
    print("Hola, es un tweets muy largo, excede los 20 caracteres")
elif len(tweet) <= 20 and len(tweet) >= 1:
    print("Tweet ha sido publicado correctamente")
else:
    print("No se puede publicar un tweet vacio")