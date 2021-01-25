import csv
import types


def export_to_file_static(path, header, data):
    with open(path, mode="a") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(data)
    # just to see if function was really called
    print(">>>> This is function export_to_file_static - static mathod")


def export_to_file_Class(cls, path):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Brand', 'Model', 'IsOnSale'])
        for car in cls.list_of_cars:
            writer.writerow([car.brand, car.model, car.IsOnSale])
    # just to see if function was really called
    print(">>>> This is function export_to_file_static - class mathod")


dir = r"D:\Python\Python_kurs_sredniozaawansowany\files"
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

    @property  # prazy pomocy property możemy nowe metody dla instancji tworzyć
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
del car01.IsOnSale  # i teraz takiego atrybutu nie mozna usunąć w zwykły sposób.
# Trzeba nową metodę i juz działa, ustawia na None
print(car03.IsOnSale)
print(car03.CarTitle)

print("Static --------------" * 10)
#  Na razie funkcja zewnętrzna spoza klasy. Trzeba ją zrobić przypisać do klasy w kolejnym wierszu
Car.Export_to_file_static = export_to_file_static
export_to_file_static(dir + '\export_static.csv', ['Brand', 'Model', 'IsOnSale'],
                      [car02.brand, car02.model, car02.IsOnSale])
Car.Export_to_file_static(dir + '\export_static01.csv', ['Brand', 'Model', 'IsOnSale'],
                          [car03.brand, car03.model, car03.IsOnSale])
print("Class --------------" * 10)
#  Car.export_to_file_Class(dir +'\export_static05.csv') # wywala błąd, trzeba import types,
# lub jako pierwszy argument nazwa klasy
Car.export_to_file_Class = types.MethodType(export_to_file_Class, Car)  # po tym juz działa, funkcja przypisuje
# funkcje jako metodę do klasy, widac to przez vars
Car.export_to_file_Class(dir + '\export_static05.csv')
print(vars(Car))