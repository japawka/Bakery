# wrapper - obudowuje funkcje inną funkcją
import datetime


def create_func_with_wrapper_log_to_file_path(logFilePath):
    def create_func_with_wrapper(func):
        def func_with_wrapper(*args, **kwargs):
            with open(logFilePath, 'a') as file:
                file.write('-' * 20 + '\n')
                file.write(f'function "{func.__name__}" started at {datetime.datetime.now().strftime("%d-%m-%Y")}\n')
                file.write("following arguments were used\n")
                file.write(' '.join(f"{x}" for x in args))
                file.write('\n')
                file.write(' '.join(f"{x} = {y}" for x, y in kwargs.items()))
                file.write('\n')
                result = func(*args, **kwargs)
                file.write(f'function returend {result}\n')
                return result

        return func_with_wrapper

    return create_func_with_wrapper


@create_func_with_wrapper_log_to_file_path('change_salary_log.txt')
def change_salary(empName, newSalary, isBonus=False):
    print(f'Changing salary for {empName} to {newSalary} as bonus = {isBonus}')
    return newSalary


@create_func_with_wrapper_log_to_file_path('change_position_log.txt')
def change_position(empName, newPosition):
    print(f'Changing position for {empName} to {newPosition}')
    return newPosition


print(change_salary("Paweł Jarzęcki", 35000, isBonus=True))
print(change_salary("Paweł Jarzęcki", 35000, True))
print(change_position("Paweł Jarzęcki", 'accountant'))
print(change_position("Jan Kowalski", 'manager'))
