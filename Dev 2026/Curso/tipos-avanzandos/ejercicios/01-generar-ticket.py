productos = [
    {"nombre": "Manzana", "precio": 0.5},
    {"nombre": "Galletas", "precio": 2.5},
    {"nombre": "Pan", "precio": 1.0},
    {"nombre": "Leche", "precio": 1.5},
]


def generar_ticket(productos):
    contador_productos = {}
    total = 0
    
    for producto in productos:
        nombre = producto["nombre"]
        if nombre in contador_productos:
            contador_productos[nombre]["cantidad"] += 1
        else:
            contador_productos[nombre] = {"precio": producto["precio"], "cantidad": 1}

    print("---------------------")
    print("Ticket de compra")
    print("---------------------")

    for nombre, info in contador_productos.items():
        precio = info["precio"]
        cantidad = info["cantidad"]
        subtotal = precio * cantidad
        total += subtotal
        print(f"{nombre} x {cantidad} - ${subtotal: .2f}")
        
    print("---------------------")
    print(f"Total: ${total: .2f}")
    print("---------------------")