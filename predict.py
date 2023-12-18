



class TrendModel():
    def predict(self, data):
        prev_value = 0
        next_value = 0
        contatore = 0
        sum = 0
        
        for item in data:
            next_value = item
            variation = next_value - prev_value
            sum += variation

            prev_value = item
            contatore += 1
        prediction = (sum / contatore) + next_value

        return prediction
    
lista = [2,3,5,6]

prossimoValore = TrendModel()

print(prossimoValore.predict(lista))
