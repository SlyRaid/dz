# Домашнее задание по уроку "Пространство имен и способы вызова функции"

# Создайте новую функцию def test... с произвольным числом параметров разного типа, функция должна распечатывать эти
# параметры внутри своего тела
# Создайте рекурсивную функцию, которая будет считать факториал от числа n, n - передается в параметре

def test(*args):
    print(*args)

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n*factorial(n-1)

print(factorial(5))
test('Привет', 1, 20, [1, 2, 45, 'Пока'])