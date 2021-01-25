# wrapper - obudowuje funkcje inną funkcją
import datetime


def create_func_with_wrapper(func):
    def func_with_wrapper(*args, **kwargs):
        print(f'function "{func.__name__}" started at {datetime.datetime.now().strftime("%d-%m-%Y")}')
        print("following arguments were used")
        print(args, kwargs)
        result = func(*args, **kwargs)
        print(f'function returend {result}')
        return result

    return func_with_wrapper


@create_func_with_wrapper  # od razu dodaje wrapper do funkcji i nie musimy juz tworzyć
# kopii funckcji z wrapperem jak w linii 27 i 32
def change_salary(empName, newSalary, isBonus=False):
    print(f'Changing salary for {empName} to {newSalary} as bonus = {isBonus}')
    return newSalary


change_salary("Paweł Jarzęcki", 35000, True)
print()

change_salary_with_log = create_func_with_wrapper(change_salary)
print(change_salary_with_log("Paweł Jarzęcki", 35000, isBonus=True))

print()
# mozemy po prostu zastąpić oryginał funkcji funkcją z wrapperem
change_salary = create_func_with_wrapper(change_salary)
print(change_salary("Paweł Jarzęcki", 35000, isBonus=True))
#albo zastosować dekorator

#############################   LAB
import time
import functools


def wrapper_time(a_function):
    def a_wrapped_function(*args, **kwargs):
        time_start = time.time()
        v = a_function(*args, **kwargs)
        time_stop = time.time()
        duration = time_stop - time_start
        print(f'Function "{a_function.__name__}" performen in {duration}')
        return v

    return a_wrapped_function


def get_sequence(n):
    v = 0
    for i in range(n):
        v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
    return v


print(get_sequence(10))

wrapped_sequence = wrapper_time(get_sequence)
print(wrapped_sequence(18))
