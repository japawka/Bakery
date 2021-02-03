import datetime as dt


class MillionDaysIterator:
    def __init__(self, date, max):
        self.date = date
        self.maxdays = max

    def __next__(self):
        if self.maxdays <= 0:
            raise StopIteration
        ret = self.date
        self.maxdays -= 1
        self.date += dt.timedelta(days=1)
        return ret

    # def __iter__(self):
    #     return self


class MIllionDays:
    def __init__(self, year, month, day, maxdays):
        self.date = dt.datetime(year, month, day)
        self.maxdays = maxdays
        self.iterator = MillionDaysIterator(self.date, self.maxdays)

    def __iter__(self):
        return self.iterator


md = MIllionDays(2000, 1, 1, 5)  # po skasowaniu metody __next__ jest bład
# TypeError: iter() returned non-iterator of type 'MIllionDays-- jak chcemy pętlę for wywołać.
# Można to naprawić dodając klasę z Iteratorem


for d in md:
    print(d)



#####################                LAB           ##################################


class CombinationsIterator:
    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers
        self.current_product = 0
        self.current_promotion = 0
        self.current_customer = 0

    def __next__(self):
        if self.current_customer >= len(self.customers):
            self.current_customer = 0
            self.current_promotion += 1

        if self.current_promotion >= len(self.promotions):
            self.current_promotion = 0
            self.current_product += 1

        if self.current_product >= len(self.products):
            self.current_product = 0
            raise StopIteration()

        item_to_return = f'{self.products[self.current_product]}, {self.promotions[self.current_promotion]}, {self.customers[self.current_customer]}'
        self.current_customer += 1
        return item_to_return


class Combinations:
    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers
        self.itarator = CombinationsIterator(self.products, self.promotions, self.customers)

    def __iter__(self):
        return self.itarator


products = [f"Product {i}" for i in range(1, 3)]
print(products)

promotions = [f"Promotion {i}" for i in range(1, 3)]
print(promotions)

customers = [f'Customer {i}' for i in range(1, 3)]
print(customers)

combinations = Combinations(products, promotions, customers)

for c in combinations:
    print(c)
for c in combinations:
    print(c)

