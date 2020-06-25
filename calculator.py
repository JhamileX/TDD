res = {
        0: 1,
        1: 1,
        2: 2,
        3: 6,
        4: 4
    }
class Calculator:

    def facUni(self, x):
        if( x < 0): 
            f = "error"
        elif(x < 5):
            f = res[x]
        else:
            f = 0
        self.facUnidad = f


    # def factorial(self, x):
    #     f = 1
    #     for i in range(1, x+1):
    #         f = f * i
    #     self.value = f