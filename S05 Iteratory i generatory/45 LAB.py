class Combinations:
    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers


    def __getitem__(self, item):

        if item >= len(self.promotions) * len(self.products) * len(self.customers):
            raise StopIteration
        else:
            pos_products = item // (len(self.promotions) * len(self.customers))
            print(pos_products)
            item = item % (len(self.promotions) * len(self.customers))
            print(item)
            pos_promotions = item // len(self.customers)
            print(pos_promotions)
            item = item % len(self.customers)
            print(item)

            pos_customers = item

            return f'{self.products[pos_products]} {self.promotions[pos_promotions]} {self.customers[pos_customers]}'




products = [f"Product {i}" for i in range(1, 4)]
promotions = [f"Promotion {i}" for i in range(1, 3)]
customers = [f'Customer {i}' for i in range(1, 6)]

combinations = Combinations(products, promotions, customers)

for i in range(0, 31):
   print(i, combinations[i])

# comb = iter(combinations)
# for c in comb:
#     print(c)