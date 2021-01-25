def buy_me(what):
    print('buy me', what)


buy_me('car')

car = buy_me  # zmienna car staje sie wywołaniem funkcji buy_me()
print(type(car))
car('pppppp')


def go_left(*args):
    print('PLACEHOLDER - turning left with', *args)  # te funkcje maja kierowac robota do stolika, zamiast print

def go_right(*args):
    print('PLACEHOLDER - turning right with', *args)

def go_forward(*args):
    print('PLACEHOLDER - going forward with', *args)

def go_back(*args):
    print('PLACEHOLDER - going back with', *args)

def stop(*args):
    print('PLACEHOLDER - stopping with', *args)

def start(*args):
    print('PLACEHOLDER - starting with', *args)

instructions = [start, go_forward, go_forward, go_left, go_forward, go_right, stop]
dish = 'zupa, schabowy i golonka'
for instr in instructions:  # wywołujemy po kolei wszystkie funkcje przy pomocy zmiennych z argumentem pizza
    instr(dish)

#####################################  LAB

def double(x):
    return 2 * x

def root(x):
    return x**2

def negaive(x):
    return -x

def div2(x):
    return x / 2

number = 8

tranformations = [double, root, div2, negaive]
tranformations2 = [root, root, div2, double]

tmp_return_number = number

for trans in tranformations2:
    tmp_return_number = trans(tmp_return_number)
    print(tmp_return_number)
