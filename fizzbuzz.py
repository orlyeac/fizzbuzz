

class FizzBuzz():

    def __init__(self):
        self.fizzbuzz = ['fizz'*(i % 3 == 0) or 'buzz'*(i % 5 == 0) or str(i) for i in range(1, 101)]
   
