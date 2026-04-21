# test_calculadora.py
# Primer test: suma de dos números positivos

def test_suma_dos_positivos():
    # ARRANGE: Preparar el escenario
    from calculadora import Calculadora
    calc = Calculadora()
    
    # ACT: Ejecutar la acción
    resultado = calc.sumar(2, 3)
    
    # ASSERT: Verificar el resultado
    assert resultado == 5