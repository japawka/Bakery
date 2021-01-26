class Car:
    number_of_cars = 0
    list_of_cars = []
    engine = 'Holden'
    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk):

        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk
        Car.number_of_cars += 1
        Car.list_of_cars.append(self)



    def is_damaged(self):
        return not (self.isAirBagOk and self.isPaintingOk and self.isMechanicOk)

    def get_info(self):
        print(f"{self.brand.upper()} {self.model.upper()}")
        print(f"Air bag     -   ok  -   {self.isAirBagOk}")
        print(f"Painting    -   ok  -   {self.isPaintingOk}")
        print(f"Mechanic    -   ok  -   {self.isMechanicOk}")
        print('---------------------------')



print('List of cars BEFORE creating instances', Car.number_of_cars, Car.list_of_cars)
car01 = Car("Seat", "Ibiza", True, True, True)
car02 = Car("Ford", "Fiesta", True, False, True)
print('List of cars AFTER creating instances', Car.number_of_cars, Car.list_of_cars)
print(id(Car), id(car01), id(car02))


print()
# mozemy sprawdzic, czy obiekt nalezy do danej klasy
print("check if object belongs to given class:", isinstance(car02, Car))
print("check if object belongs to given class by type:", type(car02))        # lub
print("check if object belongs to given class by type:", type(car02) is Car)
print("check if object belongs to given class using __class__:", car02.__class__)
print()
print("List of instane attributes with values:")
for a,b in vars(car01).items():
    print(a, '=',  b)
print('----------------')
print("List of Class attributes with values:")
for a,b in vars(Car).items():
    print(a, '=',  b)
print(dir())
print("List of instane attributes:", dir(car02))
print("List of Class attributes:  ", dir(Car))
Car.number_of_cars = 123456 # dane nie sa zabezpieczone
car02.number_of_cars = 123
print()
print("value taken from instance", car02.number_of_cars, car02.list_of_cars)
print("value taken from Class   ", Car.number_of_cars, Car.list_of_cars)
