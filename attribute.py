# Домашнее задание по уроку "Пространство имен"

# Создайте новый проект в PyCharm
# Запустите созданный проект

# Ваша задача:
# Создайте новый класс House
# Задайте ему новый атрибут numberOfFloors = 10
# В цикле пройдитесь по атрибуту numberOfFloors и распечайте значение "Текущий этаж равен"
# Полученный код напишите в ответ к домашему заданию


# class House:
#     numberOfFloors = 10
#     for i in range(1, numberOfFloors+1):
#         print(f'Текущий этаж равен {i}')

class House:
    numberOfFloors = 10

my_house = House()
for i in range(1, my_house.numberOfFloors+1):
    print(f'Текущий этаж равен {i}')