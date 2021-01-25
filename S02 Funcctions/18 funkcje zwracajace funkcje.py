def calculate(kind = '+', *args):
    result = 0
    if kind == "+":
        for a  in args:
            result += a
    elif kind == '-':
        for a in args:
            result -= a
    return result

numb = [5,6,7,4,5,6,9]

print(calculate('-', 2,2,2,2))

# funkcja tworząca funkcje zamiast tej powyżej

def create_function(kind = '+'):
    source = f'''    # f tutaj jaka poczatek f-string
def f(*args):
    result = 0
    for a in args:
        result {kind}= a    # to zamiast += lub -=
    return result
'''
    exec(source, globals()) # globals po to, zeby wynik był zwrócony do biezącego środowiska, inaczej błąd
    return f

f_add = create_function()
print(f_add(1,2,2,3,4,10))

f_subs = create_function('-')
print(f_subs(1,2,3,4,5,6,7,8,))



def add(*args):
    result = 0
    for a in args:
        result += a
    return result


#######################################  LAB
from datetime import datetime

def create_function(unit = 60):
    source = f'''  
def f(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, {unit})[0]
    '''
    exec(source, globals())
    return f
start = datetime(2019, 1, 1, 0, 0, 0)
end  = datetime.now()
f_minutes = create_function()
f_hours = create_function(3600)
f_days = create_function(86400)
print(f_days(start, end))
print(f_hours(start, end))
print(f_minutes(start, end))