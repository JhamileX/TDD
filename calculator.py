class Calculator:

    def factorial(self, x):
        f = 1
        for i in range(1, x+1):
            f = f * i
        self.value = f
    
    def facUni(self, x):
        pass