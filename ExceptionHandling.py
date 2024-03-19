# добавить обработку ValueError
def string_to_int(s):
    try:
        return int(s)
    except ValueError:
        return f'Преобразовать {s} в целое число, невозможно'

# добавить обработку FileNotFoundError, IOError
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f'Файл {filename} не найден'
    except IOError:
        return 'Ошибка ввода/вывода'

# добавить обработку ZeroDivisionError, TypeError
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Деление на 0'
    except TypeError:
        return 'Индекс должен быть целым числом'

# добавить обработку IndexError, TypeError
def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return f'Индекс {index} вне диапазона списка'
    except TypeError:
        return 'Индекс должен быть целым числом'

    