

f = lambda x: x * 2  # x jest argumentem, moze być ich więcej. ALE PO : TYLKO JEDNO WYRAŻENIE
print(f(20))

print('____________')


def generate_power_function(n):
    return lambda a: a ** n


power_3 = generate_power_function(3)
power4 = generate_power_function(4)
print(power_3(4))
print(power4(4))

list_numbers = [4, 5, 7, 112, 34, 56, 77, 9, 33, 101, 89]

filtered_list = list(filter(lambda x: x % 2 != 0, list_numbers))
print(sorted(filtered_list))

############################### LAB

text_list = ['x','xxx','xxxxx','xxxxxxx','']

f = lambda x: x.upper()
print(list(map(f, text_list)))
print(list(map(lambda x: len(x), text_list)))


f = lambda x: 'even' if x % 2 == 0 else 'odd'

print(f(5))