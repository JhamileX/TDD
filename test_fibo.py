# Cargamos el módulo unittest
import unittest  

# Importamos la clase calculadora
from calculator import Calculator

# Creamos una clase heredando de TestCase
class TestMyCalculator(unittest.TestCase):  

    def setUp(self):
        self.calc = Calculator()
    
    # Creamos una prueba para probar un valor inicial
    def test_calc1(self):
        self.calc.factorial(1)
        self.assertEqual(1, self.calc.value)
        
    def test_calc2(self):
        self.calc.factorial(0)
        self.assertEqual(2, self.calc.value)


if __name__ == '__main__':
    unittest.main()