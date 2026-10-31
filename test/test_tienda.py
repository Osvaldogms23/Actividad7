import pytest
from tienda import calcular_precio, calcular_iva

def test_calcular_precio():
    assert calcular_precio(100, 20) == 80.0
    assert calcular_precio(200, 50) == 100.0

def test_calcular_iva():
    assert calcular_iva(100) == 16.0

def test_calcular_sin_descuento():
    assert calcular_precio(150, 0) == 150.0

def test_descuento_invalido():
    with pytest.raises(ValueError):
        calcular_precio(100, 150)