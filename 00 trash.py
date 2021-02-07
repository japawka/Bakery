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
    print(i + 1, a[i])
for pos, item in enumerate(a, 1):
    print(pos, item)

print()


@createFuncWithWrapper
def fib(n):
    result = []
    a, b = 0, 1
    while len(result) <= n:
        result.append(a)
        a, b = b, a + b
    #print(result)
    print("FIbonacci ", result[n-1])


pairs = [(6, 'one'), (99, 'tworr'), (3, 'athreerrr'), (45, 'fo')]
pairs.sort(key = lambda x: x[1])
print(pairs)

my_dict = {'x': 500, 'y': 5874, 'z': 560}


for k, v in my_dict.items():
    if v == max(my_dict.values()):
        print(k, v)

fib(30)


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

print(fibo(30))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
nums1 = list(range(1, 103))
def matrix_create(list, n):
    matrix = []
    k = 0
    for i in range(len(list) // n if len(list) % n == 0 else len(list) // n + 1):
        row = []
        matrix.append(row)
        while len(row) < n:
            row.append(list[k])
            if k < len(list) - 1:
                k += 1
            else:
                break
    return matrix


my_matrix = matrix_create(nums1, 7)
for m in my_matrix:
    rowek = ''
    for member in m:
        rowek += f'{member:4}'
    print(rowek.lstrip())

# for x in range(1, 11):
# #     print(f'{x:02} {x*x:3} {x*x*x:4}')
# #
# # print('---------------------')
# # for x in range(1, 10):
# #     line = ''
# #     for y in range(1, 10):
# #         line += f"\t{x*y:2}"
# #     print(line)
# # print('---------------------------')