import datetime as dt


def MIllionDays(year, month, day, maxdays):
    date = dt.datetime(year, month, day)

    for i in range(maxdays):
        date += dt.timedelta(days=1)
        yield date


md = MIllionDays(2000, 1, 1, 6)
print(md)
for d in md:
    print(d)

################################             LAB              ###################################


def combinations(products, promotions, customers):
    for prod in products:
        for promo in promotions:
            for cust in customers:
                yield f'{prod}, {promo}, {cust}'


products = [f"Product {i}" for i in range(1, 3)]
promotions = [f"Promotion {i}" for i in range(1, 3)]
customers = [f'Customer {i}' for i in range(1, 3)]

c = combinations(products, promotions, customers)
print(next(c))
print(next(c))
print(next(c))

for d in c:
    print(d)

print(next(c))