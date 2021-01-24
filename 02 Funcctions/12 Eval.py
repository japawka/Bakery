var_x = 10
password = "My password"

source = '__import__("os").getcwd()'

# niebezpieczne jest, że ktos przez tą funkcje moze się dostać do
# tajnych rzeczy, które teoretycznie śa zaszyfrowane, czy schowane.
# Mozna się jednak zabezpieczyć
# globals = globals().copy()
# del globals['password']
globals = {}
result = eval(source, globals)
print(result)

##########################  LAB
import math
argument_list = []
for x in range(100):
    argument_list.append(x/10)

print(len(argument_list))
print(argument_list)

formula = input('podal formułę')

for x in argument_list:
    print(f'{x}{eval(formula):10.2f}')

