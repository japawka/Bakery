import fibo

v = 123, 2456, "hello"
x, y, z = v

print(z)
print(x)
print(y)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(sorted(basket))

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
   print('What is your {}?  It is {}.'.format(q, a))

fibo.fib(1000)
print(fibo.fib2(1000))