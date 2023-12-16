
#si definisca un iteratore python che generi numeri in un intervallo chiuso [a,b] divisibili per un numero x > 0


class Divisibili():
    def __init__(self, a, b, x):
        self.a = a
        self.b = b
        self.x = x
        self.i = self.a


    def __iter__(self):
        self.i = self.a
        
        return self

    def __next__(self):
        if self.i <= self.b:
            self.i += self.x
            return self.i - self.x
        else:
            raise StopIteration
    
intervallo = Divisibili(3,100,3)


#while True:
#     try:
#          print(next(intervallo))
#     except StopIteration:
#          break

 
#Vogliamo creare un iteratore che stampi tutte le potenze
#di 2, fino a che non raggiunge un esponente massimo x
#2

class Potenze2():
     def __init__(self, max):
          self.max = max
          
     def __iter__(self):
          self.n = 0
          return self
     
     def __next__(self):
          if self.n <= self.max:
               result = 2**self.n
               self.n += 1
               return result
          else:
               raise StopIteration


potenze = Potenze2(4)
numeri = iter(potenze)

#while True:
#     try:
#          print(next(potenze))
#     except StopIteration:
#          break


#flussi primi di una lista, iteratore che data una lista ne faccia uscire solo i primi


class Primi():
     def __init__(self, lista):
          self.lista = lista
     
     def __iter__(self):
          self.i = 0
          self.len = len(self.lista)
          return self
     
     def isPrimo(self, number, i):
          if i >= number:
               return True
          if number % i == 0:
               return False
          
          i = i + 1
          return self.isPrimo(number, i)
     
     def __next__(self):
          self.result = 0
          while self.i < self.len:
               if self.isPrimo(self.lista[self.i], 2) == True:
                    self.result = self.lista[self.i]
                    self.i = self.i + 1
                    return self.result
               self.i = self.i + 1
               
          raise StopIteration
     
     
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]


numeri = Primi(lista)
cercaPrimi = iter(numeri)
print(list(numeri))

while True:
     try:
          print(next(cercaPrimi))
     except StopIteration:
          break
