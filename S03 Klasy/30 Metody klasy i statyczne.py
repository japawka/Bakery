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

    def is_damaged(self):
        return not (self.isAirBagOk and self.isPaintingOk and self.isMechanicOk)

    def get_info(self):
        print(f"{self.brand.upper()} {self.model.upper()}")
        print(f"Air bag     -     ok  -   {self.isAirBagOk}")
        print(f"Painting    -     ok  -   {self.isPaintingOk}")
        print(f"Mechanic    -     ok  -   {self.isMechanicOk}")
        print(f"IS ON SALE                {self.__isOnSale}")
        print('---------------------------')

    def __get_is_on_sale(self):  # po zdefiniowaniu property IsOnSale, możemy te metody schować
        return self.__isOnSale

    def __set_is_on_sale(self, newIsOnSaleStatus):
        if self.brand == brand_on_sale:
            self.__isOnSale = newIsOnSaleStatus
            print(f"Changing status isOnSale to {newIsOnSaleStatus} for {self.brand}")
        else:
            print(f'Cannot czange staus . Sale valid for {brand_on_sale} only')

    # dodamy własciwość, która w sposób szybszy pozwoli na zmiane isOnSale, bez używania (wpisywania) metody
    IsOnSale = property(__get_is_on_sale, __set_is_on_sale, None, "if set to true - the car is available in  promo")

    @classmethod
    def read_from_text(cls, aText):
        aNewCar = cls(*aText.split(':'))
        return aNewCar

    @staticmethod
    def convert_HP_to_KW(HP):
        return HP * 0.735



line_with_list = ('Renault', 'MEgane', True, True, False, False)
line_of_text = 'Hyundai:Accent:True:True:False:True'

car05 = Car.read_from_text(line_of_text)
car04 = Car(*line_with_list)
print(car04.read_from_text(line_of_text))
car01 = Car("Opel", "Astra", True, True, True, True)
car02 = Car("Ford", "Fiesta", True, False, False)
car03 = Car("Opel", "Corsa", True, False, False)



print("---------------------------------------------------------------")
# po dodaniu property
print(car02.IsOnSale, car03.IsOnSale)
car02.IsOnSale = True
car03.IsOnSale = True

for car in Car.list_of_cars:
    car.get_info()


print('converting 120 HP to KW ', Car.convert_HP_to_KW(120))