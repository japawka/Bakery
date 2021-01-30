class Car:

    def __init__(self, brand, model, isOnSale):
        print('>>>class car init starting')
        self.brand = brand
        self.model = model
        self.__isOnSale = isOnSale
        self.name = f'{self.brand} {self.model}'
        print('>>>class Car init FINISHING')

    def __str__(self):
        return f"Brand: {self.brand}, model: {self.model}"

    def get_info(self):
        print('>>>class car get_info starting')
        super().get_info()  # to jest po to, żeby w klasie Specialist też wywołac get_info
        print(self.name.upper())
        print(f"IS ON SALE              {self.__isOnSale}")
        print('>>>class Car get_info finish')


class Specialist:
    def __init__(self, firstname, lastname, brand):
        print('>>>class Specialist init starting')
        self.firstname = firstname
        self.lastname = lastname
        self.name = f'{self.firstname} {self.lastname}'
        self.brand = brand
        print('>>>class Specialist init finishing')

    def get_info(self):
        print('>>>class Specialist get_info starting')
        print(f'{self.firstname} {self.lastname} ({self.brand})')
        print('>>>class Specialist get_info finish')


class CarSpecialist(Car, Specialist):
    def __init__(self, brand, model, isOnSale, firstname, lastname):
        print('>>>class Car_Specialist init starting')
        Car.__init__(self, brand, model, isOnSale)
        Specialist.__init__(self, firstname, lastname, brand.upper())  # brand.upper żeby nie było konfliktu z brand z Car
        print('>>>class Car_Specialist init finishing')
  #  metoda __init__ klasy Specialist została wywołana jako druga i nadpisuje metody i właściwości z klasy Car

    def get_info(self):
        print('>>>class Car_Specialist get_info starting')
        super().get_info()
        print('>>>class Car_Specialist get_info finish')

tom = CarSpecialist('Toyota', "corolla", True, "Tom", 'Smith')

print(vars(tom))
tom.get_info()

# method resolution order

print(CarSpecialist.mro())