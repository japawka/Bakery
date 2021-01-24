class Car:
    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk):
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk


car01 = Car("Seat", "Ibiza", True, True, True)
car02 = Car("Ford", "Fiesta", True, False, True)
print(car01.brand, car01.model, car01.isMechanicOk)
print(car02.brand, car02.model, car02.isMechanicOk)


################################   LAB


class Cake:
    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling


cake_01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream')
cake_02 = Cake('Chocolate muffin', 'muffin', 'chocolate', ['raisins', 'nuts'], 'cocoa')
cake_03 = Cake('Alaska Snow', 'donut', 'caramel', ['mint'], '')
bakeryOffer = [cake_01, cake_02, cake_03]
print("Today in our offer: ")
for cake in bakeryOffer:
    print(
        f'{cake.name} - ({cake.kind}), main taste: {cake.taste} with additive of {cake.additives}, filled with {cake.filling}')
