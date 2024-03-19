# Домашнее задание по уроку "Различие атрибутов класса и экземпляра"

#   Создайте новый проект в PyCharm
#   Запустите созданный проект

# Ваша задача:
#   Создайте новый класс Buiding с атрибутом total
#   Создайте инициализатор для класса Buiding, который будет увеличивать атрибут количества
# созданных объектов класса Building total (по примеру класса Lemming из урока)
#   В цикле создайте 40 объектов класса Building и выведите их на экран командой print
# Полученный код напишите в ответ к домашему заданию


class Building:
    total = 0


    def __init__(self):
        Building.total += 1


building = []
building_size = 40
while len(building) < building_size:
    my_b = Building()
    building.append(my_b)
    print(Building.total, end=' ')

