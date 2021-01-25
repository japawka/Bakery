# cache dla funkcji przechowuje w pamięci wyniki poprzednich wywołań funkcji
def silnia(top):
    x = 1
    for y in range(1, top + 1):
        x *= y
        print(y, x)
    print('silnia wynosi', x)
silnia(5)

import time
import functools

@functools.lru_cache()   # powoduje, że Python zapamietuje wyniki poprzednich obliczeń
def Factorial(n):
    time.sleep(0.1)
    if n == 1:
        return 1
    else:
        return n * Factorial(n - 1)


start = time.time()
for i in range(1, 11):
    print(f'{i}! = {Factorial(i)}')
stop = time.time()
print(stop - start)

print(Factorial.cache_info())

####################################  LAB
#@functools.lru_cache(100)
def fib(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result


start = time.time()
for i in range(1, 35):
    print(f'Fibonacci dla {i} = {fib(i)}')
    stop = time.time()
    print("execution time: ", stop - start)

stopT = time.time()
print('total time:', stopT - start)

#
# start = time.time()
# for i in range(34):
#     result = fib(i)
#     print('{0:2d} {1:8} {2:3.2f}'.format(i, result, time.time() - start))
#
# print(fib.cache_info())