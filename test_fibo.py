
import unittest  


from calculator import Calculator


class TestMyCalculator(unittest.TestCase):  

    def setUp(self):
        self.calc = Calculator()


    # def test_calc1(self):
    #     self.calc.factorial(1)
    #     self.assertEqual(1, self.calc.value)

    #     self.calc.factorial(0)
    #     self.assertEqual(1, self.calc.value)



    def test_factorial(self):
        self.calc.facUni(-51)
        self.assertEqual("error", self.calc.facUnidad)

        self.calc.facUni(1)
        self.assertEqual(1, self.calc.facUnidad)
        
        self.calc.facUni(4)
        self.assertEqual(4, self.calc.facUnidad)

        self.calc.facUni(5)
        self.assertEqual(0, self.calc.facUnidad)

        self.calc.facUni(6)
        self.assertEqual(0, self.calc.facUnidad)

        self.calc.facUni(7)
        self.assertEqual(0, self.calc.facUnidad)

        self.calc.facUni(8)
        self.assertEqual(0, self.calc.facUnidad)

        self.calc.facUni(9)
        self.assertEqual(0, self.calc.facUnidad)






    # def test_calc2(self):
    #     self.calc.factorial(0)
    #     self.assertEqual(1, self.calc.value)


if __name__ == '__main__':
    unittest.main()