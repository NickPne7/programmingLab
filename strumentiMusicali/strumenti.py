

class Strumento():
    def __init__(self, marcaStrumento, costo, proprietario):
        self.marcaStrumento = marcaStrumento
        self.costo = costo
        self.proprietario = proprietario
        
    def assegnaMusicista(self, nomeMusicista):
        self.nomeMusicista = nomeMusicista
    
    def rangeMusicale(self, min, max):
        self.min = min
        self.max = max
    
    def __str__(self):
        return "marcaStrumento: " + str(self.marcaStrumento) + " prezzo: " + str(self.costo) + " proprietario: " + str(self.proprietario)
    
    def suona(self):
        print("UUUU")
    
    def __str__(self):
        return "musicista: " + str(self.nomeMusicista) + " nome strumento: " + str(self.nomeStrumento) + "\n"




class Tastiera(Strumento):
    def rangeMusicale(self, min, max):
        return super().rangeMusicale(27, 4186)
    
    def suona(self):
        print("OOOO")
        
class Pianoforte(Tastiera):
    pass

class Sintetizzatore(Tastiera):
    pass

class Flauto(Strumento):
    def rangeMusicale(self, min, max):
        return super().rangeMusicale(261, 3349)
    

class Percussioni(Strumento):
    def suona(self):
        print("BUM!")
        
    def tipoPelleTamburi(self, tipoPelle):
        self.tipoPelle = tipoPelle
    
    
class Batteria(Percussioni):
    def suona(self):
        strumento = input("cosa vuoi suonare? crash/rullante/grancassa/tomtom/snare ")
        
        if strumento == "crash":
            print("TSSSHH!")
        elif strumento == "rullante":
            print("PRRR!")
        elif strumento == "grancassa":
            print("SBUM!")
        elif strumento == "tomtom":
            print("PUM!")
        elif strumento == "snare":
            print("PTZ!")