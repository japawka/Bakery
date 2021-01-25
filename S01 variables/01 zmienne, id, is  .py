

a = "hello PyCharm"
b = a
print(a, b)
print(a == b)
print(a is b)
print(id(a), id(b))
print()
b = a + "!!"
print(a, b)
print(a == b)
print(a is b)
print(id(a), id(b))
print()
b = b[:-2]
print(a, b)
print(a == b)
print(a is b)
print(id(a), id(b))
print()
b = a
print(a, b)
print(a == b)
print(a is b)
print(id(a), id(b))
#####################################  LAB
a = b = c = 10
print(a, id(a))
print(b, id(b))
print(c, id(c))
a = 20
print(a, id(a))
print(b, id(b))
print(c, id(c))

a = b = c = [3, 5, 7 ,8]
print(a, id(a))
print(b, id(b))
print(c, id(c))
a.append(12)
print(a, id(a))
print(b, id(b))
print(c, id(c))
print()
x = 10
y = 10
print(id(x), id(y))
y = y + 1 - 1
print(id(x), id(y))
y = y + 1234567890 - 1234567890
print(x, y)
print(id(x), id(y))