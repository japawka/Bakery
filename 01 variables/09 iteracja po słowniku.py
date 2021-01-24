# workDays = [19, 20, 21, 20, 22, 21]
# months = ['I', 'II', "III", "IV", 'V', 'VI']
#
# month_with_days = dict(zip(months, workDays))
# print(month_with_days)
#
# for key in month_with_days:
#     print(f' key is {key}, value is {month_with_days[key]}')
#
# print()
#
# for key, value in month_with_days.items():
#     print(f' key is {key}, value is {value}')

########################################   LAB

banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
dict_denominations = {coin:0 for coin in banknotes_coins}
print(dict_denominations)

dict_denominations[100] += 16
dict_denominations[20] += 145
dict_denominations[5] += 1
dict_denominations[0.5] += 121

dict_denominations[50] += 1
dict_denominations[20] += 200
dict_denominations[5] += 1
dict_denominations[2] += 20

dict_denominations[100] += 1
dict_denominations[50] += 17
dict_denominations[2] += 18

for a, b in sorted(dict_denominations.items()):
    print(f'Denominate: {a:6.2f} - amount {b:5}')

a = 1234569
b = ''
for n in str(a):
    b += str(int(n) + 1)

print((b))