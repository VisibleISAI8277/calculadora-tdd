# calculadora.py

class Calculadora:
    def sumar(self, a, b):
        return a + b
    
     
    def restar(self, a, b):
        return a - b
    


    def multiplicar(self, a, b):
        return a * b
    


    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b
    



    def raiz_cuadrada(self, numero, precision=0.001):
        """
        Calcula la raíz cuadrada usando el método de Newton-Raphson
        SIN usar librerías matemáticas.
        Solo usa suma, resta, multiplicación y división.
        """
        if numero < 0:
            raise ValueError("No se puede calcular la raíz de un número negativo")
        
        if numero == 0:
            return 0
        
        # Estimación inicial (puede ser el mismo número)
        x = numero
        
        # Iterar hasta alcanzar la precisión deseada
        while True:
            # Fórmula de Newton-Raphson: x_nuevo = (x + S/x) / 2
            x_nuevo = self.dividir(self.sumar(x, self.dividir(numero, x)), 2)
            
            # Verificar si alcanzamos la precisión deseada
            if abs(x_nuevo - x) < precision:
                return x_nuevo
            
            x = x_nuevo




              
    def exponencial(self, x, precision=0.001, max_iter=100):
        """
        Calcula e^x usando la serie de Taylor
        SIN usar librerías matemáticas.
        e^x = 1 + x + x²/2! + x³/3! + x⁴/4! + ...
        
        Cada término se calcula como: término_anterior * x / n
        """
        resultado = 1  # Primer término (n=0): x^0/0! = 1
        termino = 1    # Término actual
        
        for n in range(1, max_iter + 1):
            # Calcular siguiente término: término_anterior * x / n
            termino = self.dividir(self.multiplicar(termino, x), n)
            resultado = self.sumar(resultado, termino)
            
            # Criterio de parada: término muy pequeño
            if abs(termino) < precision:
                break
        
        return resultado