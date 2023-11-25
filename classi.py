

#classe per i file, 
class Csvfile():
    def __init__(self, name):
        self.name = name
        try:
            f = open(self.name, "r")
        except FileNotFoundError:
            print("Errore, file non found")
        
    def get_data(self):
        values = []
        file = open(self.name, "r")
        for line in file:
            elements = line.split(",")
            if elements[0] != "Data":
                p = [elements[0], elements[1][:-1]]
                values.append(p)
        file.close()
        return values


class NumericalCsvfile(Csvfile):

    def convert(self):
        lista = super().get_data()
        #assegno a lista la lista del file csv dal metodo della classe mnadre
        values = []
        contatore = 0
        
        for element in lista:
                elemento = 0
                try:
                    if element[1] != "Sales":
                        elemento = float(element[1])
                except ValueError:
                    print("non c'è un valore corrispondente alla riga")
                else:
                    values.append(float(elemento))
                    contatore = contatore + 1
                    
        print(contatore)
        return values



nome_file = "shampoo_sales.csv"

#file = Csvfile(nome_file)
fileFloat = NumericalCsvfile(nome_file)

print(fileFloat.convert())

#print(file.get_data())
