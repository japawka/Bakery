brand_on_sale = "Opel"


class Car:
    number_of_cars = 0
    list_of_cars = []

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale):
        print(self.__class__.__name__)
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk
        self.__isOnSale = isOnSale
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
        print(f"IS ON SALE              {self.__isOnSale}")
        print('--------------------------------------')

    @property  # łatwiejszy sposób na ustawianie property
    def IsOnSale(self):
        return self.__isOnSale

    @IsOnSale.setter  # żeby nie było błędu - to musimy przenieść poniżęj property
    def IsOnSale(self, newIsOnSaleStatus):  # i musimy zmienić nazwę matody na tką, jak ma property
        if self.brand == brand_on_sale:
            self.__isOnSale = newIsOnSaleStatus
            print(f"Changing status isOnSale to {newIsOnSaleStatus} for {self.brand}")
        else:
            print(f'Cannot czange status . Sale valid for {brand_on_sale} only')

    @IsOnSale.deleter
    def IsOnSale(self):
        self.__isOnSale = None


class Truck(Car):
    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale, capacityKg):
        print(self.__class__.__name__)
        super().__init__(brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale)
        # tu są dopisywane linijki  self.brand = brand itd.
        self.capacityKg = capacityKg

    def getinfo(self):
        super().get_info()
        print(f"Capacity      -         {self.capacityKg}")


cucumber = Truck("Volksvagen", "Valiant", True, True, True, False, 4000)
car01 = Truck('Ford', 'Transit', True, False, True, True, 4200)
cucumber.getinfo()
car01.getinfo()
