def aplicar_promocion(compras):
    clientes_con_promocion = []

    for cliente, monto in compras.items():
        if monto >= 150:
            clientes_con_promocion.append(cliente)
    return clientes_con_promocion