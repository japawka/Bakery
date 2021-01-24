# isOk = 0, 0, 0,
# print(isOk, type(isOk))
# if isOk:
#     print('TRUE')
# else:
#     print("FALSE")

# nawet spacja jest True
# pusty napis, tuple, lista daje False
# 0 daje false, ale lista czy tuple zer True, bo nie jest pusta, alr jeśli się
# odwołamy do konkretnego elementu listy z zerami to False

###########################################  LAB
data = {1: 'load data', 2: 'export data', 3: 'analyze & predict'}
for a, b in data.items():
    print(a, '-', b)

while True:
    userInput = input('Wybierz opcję lub naciśnij ENTER, żeby zakończyć: ')
    if userInput:
        try:
            userInput = int(userInput)
            if userInput in data:
                print(f'twój wubór to: {userInput} - {data[userInput]}')
            else:
                print("numer spoza zakresu")
        except:
            print('podaj liczbę, nie literę')
    else:
        print('koniec')
        break