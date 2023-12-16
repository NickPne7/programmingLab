

class Primo():
    def isPrimo(self, z, i):
        result = 1
        if z % i == 0:
            result = 0
            return result
        if z == i:
            return result
        i = i+1
        return isPrimo(x, i)
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 0
    

    def __iter__(self):

        return self
    
    def __next__(self):
        if isPrimo

        raise StopIteration