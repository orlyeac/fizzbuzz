

class FizzBuzz():
    
    def __init__(self, t0=1, t1=100):
        try:
            t0 = int(t0)
            t1 = int(t1)
            if t0 < t1:
                self.t0 = t0
                self.t1 = t1
            else:
                self.t0 = 1
                self.t1 = 100
                raise
        except:
            print('wrong t0 and / or t1. making t0 = 1 and t1 = 100')
        self.fizzbuzz = ['fizz'*(i % 3 == 0) + 'buzz'*(i % 5 == 0) or str(i) for i in range(self.t0, self.t1 + 1)]
        
    def at(self, p):
        try:
            intp = int(p)
        except ValueError:
            print('not an int!')
            return   
        return 'fizz'*(p % 3 == 0) + 'buzz'*(p % 5 == 0) or str(p)


if __name__ == "__main__":
    print('\n'.join(FizzBuzz().fizzbuzz))

