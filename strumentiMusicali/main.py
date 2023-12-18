from strumenti import Strumento
from strumenti import Tastiera
from strumenti import Flauto
from strumenti import Percussioni
from strumenti import Batteria



miaBatteria = Batteria("Pearl", 4000, "Nicola")
miaTastiera = Tastiera("Yamaha", 10000, "Erma")
mioFlauto = Flauto("Yamaha", 200, "Angi")

Band = [miaTastiera, miaBatteria, mioFlauto]

print("Angi suona il flauto! ")
mioFlauto.suona()

print("nicola, vai a tempo")
miaBatteria.suona()




