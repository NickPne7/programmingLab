



class Date():
    def __init__(self, giorno, mese, anno):
        try:
            self.giorno = giorno
            self.mese = mese
            self.anno = anno
        except self.giorno > 31 or self.mese > 12:
            return "Anno o mese invalido"
    
    def convertiBisestile(self):
        if self.mese == 2:
            self.maxMese = 29
        
        return NotImplementedError
    
    #controllo se l'anno è bisestile o no
    def bisestileCheck(self, anno):#
        if anno % 400 == 0 or anno % 4 == 0 and anno % 100 != 0:
            return True
        else:
            return False
    
    #da inizializzazione ai giorni del mese corrente
    def giorniMese(self): 
        if self.mese % 2 != 0 or self.mese == 8 or self.mese == 10 or self.mese == 12:
            giorni = 31
        #gestisco febbraio
        elif self.mese == 2:
            if self.bisestileCheck(self.anno):
                giorni = 29
            else:
                giorni = 28
        else:
            giorni = 30
            
        return giorni
    
    def __str__(self):
        return "giorno: " + str(self.giorno) + " mese: " + str(self.mese) + " anno: " + str(self.anno) + "\n"
    
    def __iter__(self):
        self.incremento = 1
        self.maxMese = self.giorniMese()
        self.mesiInAnno = 12
        
        return self
    
    #serve per testing
    def ritornaMax(self):
        return self.maxMese
    
    
    def __next__(self):
        self.giorno += 1
        
        #resetto al nuovo giorno
        if self.giorno > self.maxMese:
            self.mese += 1
            self.maxMese = self.giorniMese()
            self.giorno = 1
            #controllo il mese, per cambiare anno in caso
            if self.mese > self.mesiInAnno:
                self.mese = 1
                self.anno += 1
                
        return self.giorno
    