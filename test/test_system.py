import pytest
from tienda import calcular_precio, calcular_iva

# --- PRUEBAS DE INTEGRACIÓN Y SISTEMA ---

def test_flujo_compra_exitoso_try():
    """Prueba de integración: Simula un flujo completo exitoso (TRY)"""
    precio_inicial = 500.0
    porcentaje_desc = 20.0
    
    # Paso 1: Aplicar descuento
    precio_con_descuento = calcular_precio(precio_inicial, porcentaje_desc)
    assert precio_con_descuento == 400.0
    
    # Paso 2: Aplicar IVA sobre el precio con descuento
    iva = calcular_iva(precio_con_descuento)
    assert iva == 64.0
    
    # Paso 3: Total del sistema
    total_sistema = precio_con_descuento + iva
    assert total_sistema == 464.0

def test_flujo_compra_error_exception():
    """Prueba de integración: Simula un flujo que falla y lanza una EXCEPTION"""
    precio_invalido = -100.0
    descuento = 10.0
    
    # Validamos que al intentar procesar un precio negativo se capture la excepción esperada
    with pytest.raises(ValueError) as excinfo:
        calcular_precio(precio_invalido, descuento)
    
    assert "Valores inválidos" in str(excinfo.value)