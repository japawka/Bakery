brand_on_sale = "Opel"


class Car:
    number_of_cars = 0
    list_of_cars = []

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale=False):
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk
        Car.number_of_cars += 1
        Car.list_of_cars.append(self)
        self.__isOnSale = isOnSale  # ta kapnstrukcja zabezpiecza przed zmianami z zewnątrz,
        # po otworzeniu obiektu

    def get_info(self):
        print(f"{self.brand.upper()} {self.model.upper()}")
        print(f"Air bag     -     ok  -   {self.isAirBagOk}")
        print(f"Painting    -     ok  -   {self.isPaintingOk}")
        print(f"Mechanic    -     ok  -   {self.isMechanicOk}")
        print(f"IS ON SALE                {self.__isOnSale}")
        print('---------------------------')

    def __get_is_on_sale(self):  # po zdefiniowaniu property IsOnSale, możemy te metody schować
        return self.__isOnSale

    # IsOnSale = property(__get_is_on_sale, __set_is_on_sale, None, "if set to true - the car is available in  promo")

    @property  # łatwiejszy sposób na ustawianie property
    def IsOnSale(self):
        return self.__isOnSale

    @IsOnSale.setter  # żeby nie było błędu - to musimy przenieść poniżęj property
    def IsOnSale(self, newIsOnSaleStatus):  # i musimy zmienić nazwę matody na tką, jak ma property
        if self.brand == brand_on_sale:
            self.__isOnSale = newIsOnSaleStatus
            print(f"Changing status isOnSale to {newIsOnSaleStatus} for {self.brand}")
        else:
            print(f'Cannot czange staus . Sale valid for {brand_on_sale} only')

    @IsOnSale.deleter
    def IsOnSale(self):
        self.__isOnSale = None

    @property   # prazy pomocy property możemy nowe metody dla instancji tworzyć
    def CarTitle(self):
        return (f"Brand: {self.brand.title()}, nodel: {self.model.title()}")


car01 = Car("Opel", "Astra", True, True, True, True)
car02 = Car("Ford", "Fiesta", True, False, False)
car03 = Car("Opel", "Corsa", True, False, False)

for car in Car.list_of_cars:
    car.get_info()

print(car03.IsOnSale)
car03.IsOnSale = True
car02.IsOnSale = True
print(car03.IsOnSale)
del car03.IsOnSale  # i teraz takiego atrybutu nie mozna usunąć w zwykły sposób.
# Trzeba nową metodę i juz działa, ustawia na None
print(car03.IsOnSale)
print(car03.CarTitle)
