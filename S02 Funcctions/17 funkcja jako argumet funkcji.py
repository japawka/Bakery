# def bake(what):
#     print(f'baking {what}')
#
#
# def add(what):
#     print(f'adding {what}')
#
#
# def mix(what):
#     print(f'mixing {what}')
#
#
# cookbook = [(add, 'milk'), (add, 'eggs'), (add, 'sugar'), (add, 'flour'), (mix, 'ingredients'), (bake, 'cookies')]
#
# for activity, obj in cookbook:
#     activity(obj)
#
#
# def cook(activity, obj):
#     activity(obj)
#
#
# cook(bake, 'cookies')
#
#
# for activity, obj in cookbook:
#     cook(activity, obj)
######################################   LAB
def double(x):
    return 2 * x

def root(x):
    return x**2

def negative(x):
    return -x

def div2(x):
    return x / 2

def generate_values(function, listOfNumbers):
    generatednumbers = []
    for num in listOfNumbers:
       generatednumbers.append(function(num))
    return generatednumbers

x_table = list(range(1, 12))
print(generate_values(double, x_table))
print(generate_values(root, x_table))
print(generate_values(negative, x_table))
print(generate_values(div2, x_table))