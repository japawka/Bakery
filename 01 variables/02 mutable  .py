number = 10
print(number, id(number))

number = 112
print(number, id(number))  # w immutable po zmianie wartości zmienia się tez id,
# czyli zmienia się adres w pamięci, a nie dane we tym samym obszarze pamięci
# number po zmianie wartości jest juz inną zmienną

lista = ['Hello', 'Kazik']  # lista jest mutable, adres zastaje ten sam
print(lista, id(lista))

list_2 = lista
print(list_2, id(list_2))

list_2.append('12')  # a to dodaje element do obu lista, bo obie listy wskazują na
# ten sam obszar pamięcii id cały czas to samo zostaje
print(lista, id(lista))
print(list_2, id(list_2))

napisa = [1, 2, 3]
napis_2 = napisa.copy()  # teraz to będzie kopia z innym id
print(napisa, id(napisa))
print(napis_2, id(napis_2))
napis_2.append(12)
print(napisa, id(napisa))
print(napis_2, id(napis_2))

################################################### LAB

days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
workdays = days.copy()
workdays.pop()
workdays.pop()
print(days)
print(workdays)
