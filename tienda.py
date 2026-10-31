def calcular_precio(precio_base, porcentaje_descuento):
    if precio_base < 0 or porcentaje_descuento < 0 or porcentaje_descuento > 100:
        raise ValueError("Valores inválidos")
    descuento = precio_base * (porcentaje_descuento / 100)
    return precio_base - descuento

def calcular_iva(precio):
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    return precio * 0.16