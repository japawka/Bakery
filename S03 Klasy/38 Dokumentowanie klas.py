brand_on_sale = "Opel"

class Car:
    """
        Class operating on Cars in shop
    """

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale=False):
        """
        :param brand:  brand od car
        :param model:
        :param isAirBagOk: Was it used or not
        :param isPaintingOk:
        :param isMechanicOk:
        :param isOnSale:
        """
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk

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

    @property
    def IsOnSale(self):
        """IsOnSale - The car is on extra promotion. Valid only for cars in list 'brand_on_sale' """
        return self.__isOnSale

    @IsOnSale.setter
    def IsOnSale(self, newIsOnSaleStatus):
        if self.brand == brand_on_sale:
            self.__isOnSale = newIsOnSaleStatus
            print(f"Changing status isOnSale to {newIsOnSaleStatus} for {self.brand}")
        else:
            print(f'Cannot czange staus . Sale valid for {brand_on_sale} only')

    @IsOnSale.deleter
    def IsOnSale(self):
        self.__isOnSale = None

help(Car)
help(Car.IsOnSale)
