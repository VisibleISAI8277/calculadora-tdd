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





# Tests para división

def test_dividir_dos_positivos():
    from calculadora import Calculadora
    calc = Calculadora()
    assert calc.dividir(10, 2) == 5

def test_dividir_negativos():
    from calculadora import Calculadora
    calc = Calculadora()
    assert calc.dividir(-10, -2) == 5

def test_dividir_por_cero():
    from calculadora import Calculadora
    calc = Calculadora()
    try:
        calc.dividir(10, 0)
        assert False, "Debería lanzar ValueError"
    except ValueError:
        assert True

def test_dividir_decimales():
    from calculadora import Calculadora
    calc = Calculadora()
    assert abs(calc.dividir(7, 2) - 3.5) < 0.001




# Tests para raíz cuadrada (sin usar math.sqrt)

def test_raiz_cuadrada_4():
    from calculadora import Calculadora
    calc = Calculadora()
    # √4 = 2, con precisión de 0.001
    assert abs(calc.raiz_cuadrada(4) - 2) < 0.001

def test_raiz_cuadrada_9():
    from calculadora import Calculadora
    calc = Calculadora()
    # √9 = 3
    assert abs(calc.raiz_cuadrada(9) - 3) < 0.001

def test_raiz_cuadrada_2():
    from calculadora import Calculadora
    calc = Calculadora()
    # √2 ≈ 1.414
    assert abs(calc.raiz_cuadrada(2) - 1.414) < 0.001

def test_raiz_cuadrada_cero():
    from calculadora import Calculadora
    calc = Calculadora()
    # √0 = 0
    assert calc.raiz_cuadrada(0) == 0

def test_raiz_cuadrada_negativo():
    from calculadora import Calculadora
    calc = Calculadora()
    # La raíz de negativo debe lanzar error
    try:
        calc.raiz_cuadrada(-4)
        assert False, "Debería lanzar ValueError para números negativos"
    except ValueError:
        assert True