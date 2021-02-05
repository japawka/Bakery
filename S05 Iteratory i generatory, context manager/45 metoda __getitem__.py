import datetime as dt


class MIllionDays:
    def __init__(self, year, month, day, maxdays):
        self.date = dt.datetime(year, month, day)
        self.maxdays = maxdays

    def __getitem__(self, item):
        if item <= self.maxdays:
            return self.date + dt.timedelta(days=item)
        else:
            raise StopIteration

md = MIllionDays(2000,1,1,25)

print(md[3])
#print(next(md))  # daje bład
for d in md: #  teraz to juz działa, choć nie zdefiniowalismy __iter__
    print(d)
 # W tej chwili klas nie jest iteratorem, bo nie ma zdefiniowanej metody NEXT.
# Trzeba dka niej stworzyć sztuczny iterator. Ale musi być metoda __getitem__

it = iter(md)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))