


class divisibili():
    def __init__(self, a, b, x):
        self.a = a
        self.b = b
        self.x = x
        self.i = self.a

    def __iter__(self):
        self.i = self.aSS
        
        return self

    def __next__(self):
        if self.i <= self.b:
            self.i += self.x
            return self.i - self.x
        else:
            raise StopIteration
    
intervallo = divisibili(3,100,3)



 
