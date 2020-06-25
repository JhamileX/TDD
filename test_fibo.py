
import unittest  


from calculator import Calculator


class TestMyCalculator(unittest.TestCase):  

    def setUp(self):
        self.calc = Calculator()


    def test_calc1(self):
        self.calc.factorial(1)
        self.assertEqual(1, self.calc.value)
        self.calc.factorial(0)
        self.assertEqual(1, self.calc.value)


    # def test_calc2(self):
    #     self.calc.factorial(0)
    #     self.assertEqual(1, self.calc.value)


if __name__ == '__main__':
    unittest.main()