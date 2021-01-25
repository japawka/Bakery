# for i in range(10, 0, -1): # od tyłu, ale wtedy musimy podać -1, jezeli każdy element.
#     print(i)
# lista = "AGCDEFG"
# a = {a:b for a, b in zip(range(len(lista)), lista)}
# print(a)
#
# listka = list(range(10))
# print(listka[-1:0])  # lista od tyłu, ale wtedy musimy podać -1, jezeli każdy element.
# # Bez tego pusta lista
# print(listka[-1:0:-1])
# print(listka[-1::-1]) #lista odwrócona
# print(listka[::2]) # lista cała co drugi element
# print(listka[1::2]) # lista os indeksu 1 co drugi element
#
# lista2 = listka.copy()
# lista3 = listka[:]
# lista4 = list(listka)
# print(id(listka))
# print(id(lista2))
# print(id(lista3))
# print(id(lista4))
############################################## LAB
colors = ["red", "orange", "green", "violet", "blue", "yellow"]

def get_colors_list(colorsList, n):
    return colorsList[:n]

for i in range(1, len(colors) + 1):
    print(get_colors_list(colors, i))


text = '''Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką 
prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W 
rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi 
w niej prawo dżungli. '''

short = text[text.index('(') + 1: text.index(')')]
print(short)
