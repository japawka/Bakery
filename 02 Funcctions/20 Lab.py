import os
from datetime import datetime as dt


def wrapper_with_log_file(logged_action, log_file_path):
    def wrapper_with_log_to_known_file(func):
        def reaL_wrapper(path):
            with open(log_file_path, 'a') as file:
                file.write('-' * 20 + '\n')
                file.write(
                    f'Performed {logged_action} on file {path} started at {dt.now().strftime("%d-%m-%Y %H:%M:%S")}\n')
                return func(path)

        return reaL_wrapper

    return wrapper_with_log_to_known_file


@wrapper_with_log_file('FILE_CREATE', 'file_create.txt')
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+")


@wrapper_with_log_file('FILE_DELETE', 'file_delete.txt')
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


create_file('dummy_file.txt')
delete_file('dummy_file.txt')
create_file('dummy_file.txt')
delete_file('dummy_file.txt')
