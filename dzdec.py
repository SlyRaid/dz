# Цель задания:
#   Освоить механизмы создания декораторов Python.
#   Практически применить знания, создав функцию декоратор и обернув ею другую функцию.
#
# Задание:
# Напишите 2 функции:
#   Функция которая складывает 3 числа (sum_three)
#   Функция декоратор (is_prime), которая распечатывает "Простое",
# если результат 1ой функции будет простым числом и "Составное" в противном случае.



def is_prime(func):
    def wrapper(*args, **kwargs):
        results = func(*args, **kwargs)
        k = 0
        for i in range(2, results // 2 + 1):
            if (results % i == 0):
                k = k + 1
        if (k <= 0):
            print("Число простое")
        else:
            print("Число не является простым")
    return wrapper

@is_prime
def sum_three(a, b, c):
    s = a + b + c
    return s

result = sum_three(3, 3, 6)


