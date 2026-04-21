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





    
# Primer test: resta de dos números positivos
def test_resta_dos_positivos():
    # ARRANGE: Preparar el escenario
    from calculadora import Calculadora
    calc = Calculadora()
    
    # ACT: Ejecutar la acción
    resultado = calc.restar(5, 3)
    
    # ASSERT: Verificar el resultado
    assert resultado == 2

def test_resta_negativos():
    # ARRANGE
    from calculadora import Calculadora
    calc = Calculadora()
    
    # ACT
    resultado = calc.restar(-5, -3)
    
    # ASSERT
    assert resultado == -2

def test_resta_cero():
    # ARRANGE
    from calculadora import Calculadora
    calc = Calculadora()
    
    # ACT
    resultado = calc.restar(5, 0)
    
    # ASSERT
    assert resultado == 5






# Tests para multiplicación

def test_multiplicar_dos_positivos():
    from calculadora import Calculadora
    calc = Calculadora()
    assert calc.multiplicar(3, 4) == 12

def test_multiplicar_negativos():
    from calculadora import Calculadora
    calc = Calculadora()
    assert calc.multiplicar(-3, -4) == 12

def test_multiplicar_por_cero():
    from calculadora import Calculadora
    calc = Calculadora()
    assert calc.multiplicar(5, 0) == 0

def test_multiplicar_por_uno():
    from calculadora import Calculadora
    calc = Calculadora()
    assert calc.multiplicar(7, 1) == 7