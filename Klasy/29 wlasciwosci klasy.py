 #  Atrybut isOnSale będzie mozna zmienic tylko dla samochodów w promocji
brand_on_sale = "Opel"

class Car:
    number_of_cars = 0
    list_of_cars = []

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale = False):
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk
        Car.number_of_cars += 1
        Car.list_of_cars.append(self)
        self.__isOnSale = isOnSale  # ta kapnstrukcja zabezpiecza przed zmianami z zewnątrz,
        # po otworzeniu obiektu

    def is_damaged(self):
        return not (self.isAirBagOk and self.isPaintingOk and self.isMechanicOk)

    def get_info(self):
        print(f"{self.brand.upper()} {self.model.upper()}")
        print(f"Air bag     -     ok  -   {self.isAirBagOk}")
        print(f"Painting    -     ok  -   {self.isPaintingOk}")
        print(f"Mechanic    -     ok  -   {self.isMechanicOk}")
        print(f"IS ON SALE                {self.__isOnSale}")
        print('---------------------------')

    def __get_is_on_sale(self): # po zdefiniowaniu property IsOnSale, możemy te metody schować
        return self.__isOnSale

    def __set_is_on_sale(self, newIsOnSaleStatus):
        if self.brand == brand_on_sale:
            self.__isOnSale = newIsOnSaleStatus
            print(f"Changing status isOnSale to {newIsOnSaleStatus} for {self.brand}")
        else:
            print(f'Cannot czange staus . Sale valid for {brand_on_sale} only')

    # dodamy własciwość, która w sposób szybszy pozwoli na zmiane isOnSale, bez używania (wpisywania) metody
    IsOnSale = property(__get_is_on_sale, __set_is_on_sale, None, "if set to true - the car is available in  promo")


car01 = Car("Opel", "Astra", True, True, True, True)
car02 = Car("Ford", "Fiesta", True, False, False)
car03 = Car("Opel", "Corsa", True, False, False)

print(car01._Car__get_is_on_sale(), car03._Car__get_is_on_sale()) # jak nie zapiszemy tak, to teraz błąd wywali
# car03.set_is_on_sale(True)
# car01.set_is_on_sale(True)
#print(car01.get_is_on_sale(), car03.get_is_on_sale())

print()
# po dodaniu property
print(car02.IsOnSale, car03.IsOnSale)
car02.IsOnSale = True
car03.IsOnSale = True
print(car02.IsOnSale, car03.IsOnSale)