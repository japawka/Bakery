import datetime as dt
import sys

start = dt.datetime.now()
print(f'Execution started at: {start}')

#
# dates = [dt.datetime(2000, 1, 1) + dt.timedelta(days = i) for i in range(2500000)]
# print("The size of dates is", sys.getsizeof(dates))
# for d in dates:
#     pass
# pęttlę powyżej zastapimy iteratorem
#
class MIllionDays:
    def __init__(self, year, month, day, maxdays):
        self.date = dt.datetime(year, month, day)
        self.maxdays = maxdays

    def __next__(self):
        if self.maxdays <= 0:
            raise StopIteration()
        ret = self.date
        self.date += dt.timedelta(days=1)
        self.maxdays -= 1
        return ret

    def __iter__(self): # ma zwrócić obietkt, który mas metodę next, ale że ją juz mamy to
        # wystarczy zwrócić self
        return self


md = MIllionDays(2000, 1, 1, 250000)
print("The size of MIllionDays object is", sys.getsizeof(md))
print(next(md))
print(next(md))
print(next(md))
for i in range(25):
    print(next(md))

for d in md:  # na razie bład, bo md nie jest iterable. Trzeba dodać  metodę "iter " w klasie
    pass
md = MIllionDays(2000, 1, 1, 250000)

stop = dt.datetime.now()
print(f'Execution stopped at: {stop}')
print(f"Total time: {stop - start}")
