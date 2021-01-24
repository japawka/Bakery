import time
source = 'reportLine += 1'

 # compile przetwarza zmienną source z tekstu do postaci binarnej, przedtem przy każdym wywołaniu
# tekst musiał byc kompilowany, po wykorzystaniu funkcji compile() już nie
compiledSource = compile(source, 'source', 'exec')

reportLine = 0
start = time.time()
for i in range(100000):
    exec(source)
stop = time.time()
not_comp_time = stop - start


start = time.time()
for i in range(100000):
    exec(compiledSource)
stop = time.time()
comp_time = stop - start

print(not_comp_time, comp_time)
print(not_comp_time / comp_time)

print(reportLine)


#####################################  LAB
import math
formulas_list = [
     "abs(x ** 3 - x ** 0.5)",
     "abs(math.sin(x) * x**2)"
     ]

argument_list = []

for i in range(1000000):
    argument_list.append(i/10)

for formula in formulas_list:
    result_list = []
    print(formula)
    start = time.time()
    for x in argument_list:
        result_list.append(eval(formula))
    print(f'min: {min(result_list)}, max: {max(result_list)}')
    stop = time.time()
    print("Calculation time: {}".format(stop - start))

for formula in formulas_list:
    formula_compiled = compile(formula, "variable formula", "eval")
    result_list = []
    print(formula)
    start = time.time()
    for x in argument_list:
        result_list.append(eval(formula_compiled))
    print(f'min: {min(result_list)}, max: {max(result_list)}')
    stop = time.time()
    print("Calculation time: {}".format(stop - start))

