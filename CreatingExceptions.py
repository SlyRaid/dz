# Цель задания:
#   Освоить механизмы создания и обработки исключений в Python.
#   Научиться создавать собственные исключения, наследуя классы от Exception.
# Попрактиковаться в передаче исключений дальше по стеку вызовов.
#
# Задание:
#   Создайте новый проект или продолжите работу в текущем проекте.
#   Создайте минимум два своих собственных исключения, наследуя их от класса Exception.
# Например, InvalidDataException и ProcessingException.
#   Напишите функцию, которая генерирует различные исключения в зависимости от передаваемых ей аргументов.
#   Добавьте обработку исключений в функции, вызывающие вашу функцию, и передайте исключения дальше по стеку вызовов.
#   В основной части программы вызовите эти функции и корректно обработайте
#
# Комментарии к заданию:
#   Важно понять разницу между обработкой исключений (блок try/except) и их генерацией (оператор raise).
#   Дополнительно: попробуйте использовать блоки finally или else для дополнительных действий при обработке исключений.
#   Обратите внимание на то, как исключения передаются по стеку вызовов и как это можно использовать
# для стратегии обработки ошибок в сложных программах.
#   Важно!! Для передачи обработанных исключений в вызвавшую функцию, нужно вызывать raise



class MyExc_1(Exception):
    pass

class MyExc_2(Exception):
    pass

def gen_exc(arg):
    if arg == 0:
        raise MyExc_1('Исключение 1!')
    if arg < 5:
        raise MyExc_2('Исключение 2!')

try:
    gen_exc(6)
except MyExc_1 as e:
    print(f'Произошла ошибка: {e}')
except MyExc_2 as e:
    print(f'Ошибка: {e}')
else:
    print('Все хорошо!')
finally:
    print('Закончили')
