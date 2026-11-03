from tienda import calcular_precio, calcular_iva

def procesar_compra(precio, descuento):
    try:
        precio_con_desc = calcular_precio(precio, descuento)
        monto_iva = calcular_iva(precio_con_desc)
        total_final = precio_con_desc + monto_iva
        print(f"Compra exitosa. Total a pagar con IVA: ${total_final}")
        return total_final
    except ValueError as e:
        print(f"Error en el proceso de compra: {e}")
        raise e

if __name__ == "__main__":
    # Ejemplo de ejecución normal
    procesar_compra(200, 10)