import datetime


def createFuncWithWrapper(func):
    def functionWirthWrapper(*args, **kwargs):
        print("started :", datetime.datetime.now())
        result = func(*args, **kwargs)
        print("End od func")
        return result

    return functionWirthWrapper


a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
for pos, day in enumerate(a, 1):
    print(pos, day)

print()


@createFuncWithWrapper
def fib(n):
    result = []
    a, b = 0, 1
    while len(result) <= n:
        result.append(a)
        a, b = b, a + b
    print(result)
    print("FIbonacci ", result[n-1])


pairs = [(6, 'one'), (99, 'tworr'), (3, 'athreerrr'), (45, 'fo')]
pairs.sort(key = lambda x: x[1])
print(pairs)

my_dict = {'x': 500, 'y': 5874, 'z': 560}


for k, v in my_dict.items():
    if v == max(my_dict.values()):
        print(k, v)

fib(100)


matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]

]

rows = [[row[i] for row in matrix] for i in range(4)]
print("rows", rows)
mart = [[r[i] for r in rows] for i in range(3)]

print("mart", mart)

next_lst = list(zip(*matrix))
print(next_lst)

matrix2 = [[j for j in range(8)] for i in range(2)]
print(matrix2)

numbers = [1.5, 3.2, 4.3]
print(sorted(numbers, key=lambda x: x - int(x)))  # [3.2, 4.3, 1.5]

numbers = [1, 2, 3, 4, 5]
for number in reversed(numbers):
    print(number)

def fibo(n):
    if n <= 1:
        result = n
    else:
        result = fibo(n - 1) + fibo(n - 2)

    return result

print(fibo(10))

nums = [1,2,3,4,5,6,7,8,9,10,11,12]
mat = []
k = 0
for i in range(3):
    row = []
    mat.append(row)
    while len(row) < 3:
        row.append(nums[k])
        k += 1
print(mat)