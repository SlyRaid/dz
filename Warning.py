# Цель задания:
#
#     Освоить механизмы создания и обработки исключений в Python.
#     Научиться создавать собственные исключения, наследуя классы от Exception.
# Попрактиковаться в передаче исключений дальше по стеку вызовов.
#
# Задание:
#
#     Импортируйте модуль warnings.
#     Реализуйте функцию для расчёта деления, которая будет генерировать предупреждение,
# если делитель близок к нулю (например, меньше 0.01), предупреждая об опасности деления на ноль.
#     Сгенерируйте UserWarning в этом случае.
#     Используйте разные фильтры для управления поведением программы при появлении такого
# предупреждения: always, ignore, error
#
#
#     Комментарии к заданию:
#
#     Предупреждения часто используются для информирования о ситуациях, которые не являются критическими ошибками,
# но могут привести к потенциальным проблемам (например, устаревание использованного API или
# непредвиденное использование функции).
#     В отличие от исключений, предупреждения не останавливают выполнение программы,
# но предоставляют полезную информацию разработчикам.

import warnings

def closeZero(a, b):

    if b != 0:
        s = a / b
        if s <= 0.01:
            warnings.warn('Приближаешься к нулю!!!', category=UserWarning)
        return print(s)

# warnings.simplefilter("always")
# warnings.simplefilter("ignore")
# warnings.simplefilter("error")

try:
    for i in range(0, 121, 20):
        closeZero(a=1, b=i)
except UserWarning as e:
    print('СЛОВИЛ')

