def returnAbajo(n):
    promedio = sum(n)/len(n)
    abajo = []
    for i in range(0,len(n)):
        if n[i] < promedio:
            abajo.append(n[i])
    return abajo
