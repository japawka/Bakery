import random
def random_with_sum(number_of_values, asserted_sum):

    numbers = list(range(number_of_values))
    while True:
        for i in range(number_of_values):
            numbers[i] = (random.randint(1, 101))
            if sum(numbers) == asserted_sum:
                yield numbers




s = random_with_sum(3, 100)
for i in range(10):
    print(next(s))

