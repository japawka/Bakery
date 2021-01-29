class Car:
    number_of_cars = 0
    list_of_cars = []

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk, accesories):

        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk
        self.accesories = accesories
        Car.number_of_cars += 1
        Car.list_of_cars.append(self)

    def __str__(self):
        return f"Brand: {self.brand}, model: {self.model}"

    def is_damaged(self):
        return not (self.isAirBagOk and self.isPaintingOk and self.isMechanicOk)

    def get_info(self):
        print(f"{self.brand.upper()} {self.model.upper()}")
        print(f"Air bag     -   ok  -   {self.isAirBagOk}")
        print(f"Painting    -   ok  -   {self.isPaintingOk}")
        print(f"Mechanic    -   ok  -   {self.isMechanicOk}")
        print(f"Accesories              {self.accesories}")
        print('---------------------------', id(self))


    # def __iadd__(self, other): # ten operator odpowiada znakowi +=
    #     if type(other) is list:
    #         accesories = self.accesories
    #         accesories.extend(other)
    #         return Car(self.brand, self.model, self.isAirBagOk, self.isPaintingOk, self.isMechanicOk, self.accesories)
    #     elif type(other) is str:
    #         accesories = self.accesories
    #         accesories.append(other)
    #         return Car(self.brand, self.model, self.isAirBagOk, self.isPaintingOk, self.isMechanicOk, self.accesories)
    #     else:
    #         raise Exception(f'Adding type  {type(other)} is not implemented')

    def __iadd__(self, other): # ten operator odpowiada znakowi +=
        if type(other) is list:
            self.accesories.extend(other)
            return self
        elif type(other) is str:
            self.accesories.append(other)
            return self
        else:
            raise Exception(f'Adding type  {type(other)} is not implemented')



    def __add__(self, other):  # mozna dodać do siebie 2 samochody - zwróci listę
        if type(other) is Car:
            return [self, other]
        else:
            raise Exception(f'Adding type  {type(other)} is not implemented')




car01 = Car("Seat", "Ibiza", True, True, True, ['winter tires'])

car02 = Car("Ford", "Fiesta", True, False, True, ['Cd player'])
car02.get_info()
car02.__iadd__('navigation')
car02.get_info()
car02 += 'car audio'
car02.get_info()
car02 += 'Roof rack'





