# test_sample.py

def test_sum():
    """Prueba básica para verificar suma."""
    assert 2 + 2 == 4

def test_subtraction():
    """Prueba básica para verificar resta."""
    assert 5 - 3 == 2

def test_failure():
    """Esta prueba fallará intencionalmente para validar pytest."""
    assert 2 * 2 == 5  # Esto está diseñado para fallar