
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



nome_file = "shampoo_sales.csv"
file = Csvfile(nome_file)

print(file.get_data())
