class Car:
    number_of_cars = 0
    list_of_cars = []

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale):
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


car01 = Car("Seat", "Ibiza", True, True, True, False)
car02 = Car("Ford", "Fiesta", True, False, True, False)

car02.isOnSale = True  # Teraz nie bedzie juz działać, nawet sięni pojawia w podpowiedziach,
# chba że sie dostaniemy przez     _Car__isOnSale
car02.get_info()
car02.year_of_production = 123456789  # ten atrybut dodaliśmy do obiektu tylko, widać go przez vars(),
# przez get_info() nie widać. Mozna go też usunąć. Dodawać można też prezez setattr.
# sprawdzić, czy obiekt ma atrybut przez hasattrI
setattr(car01, "engine", "HOLDEN")
print(hasattr(car01, 'engine'))
delattr(car01, "engine")
del car02.isMechanicOk
car01.get_info()

print("List of Class attributes with values:")  # a tu widac dwa razy isOnSale,
# jako atrybut klasy i atrybut instancji. Atrybut klasy pozostał niezmieniony
# a jego została jakby zamienioana na _Car__isOnSale
for a, b in vars(car01).items():
    print(a, '=', b)
