import itertools as it

my_list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
my_list2 = ['a', 'b', 'c', 'd']
couter = 1
for combination in it.combinations(my_list2, 5):  # kombinacje wszystkie mozliwe robi, jako drugi argument liczba  elenentów w kombinacji
    print(couter, combination)
    couter += 1

counter = 1
for combination in it.permutations(my_list2, 3):  # kombinacje wszystkie mozliwe robi, ale powtarza elementy i po kolei kazdy pierwszy
    print(counter, combination)
    counter += 1

counter = 1
for combination in it.combinations_with_replacement(my_list2, 3):  # kombinacje wszystkie mozliwe robi, ale tu wybrany element moze być powtórnie wybtany
    print(counter, combination)
    counter += 1

money = [20, 20, 20, 20, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

results = []
for i in range(1, 101):
    for combination in it.combinations(money, i):
        if sum(combination) == 100:
            results.append(combination)
results = set(results)
for r in results:
    print(r)


wallet = [50, 20, 10, 5]
for i in range(1, 101):
    for combination in it.combinations_with_replacement(wallet, i):
        if sum(combination) == 100:
            print(combination)


from math import factorial as fact

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
counter = 1
for per in it.permutations(notes, 4):
    print(counter, per)
    counter += 1
war = fact(7) / fact(7-4)
print(war)

counter = 1
for per in it.product(notes, repeat=4):
    print(counter, per)
    counter += 1
print(pow(7, 4))

