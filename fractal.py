import simple_draw as sd

sd.resolution = (1200, 600)
# нарисовать ветку дерева из точки (300, 5) вертикально вверх длиной 100

point_0 = sd.get_point(300, 5)

# сделать функцию рисования ветки из заданной точки, с заданной длины, с заданным наклоном

# def branch(point, angle, lenght):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=lenght, width=3)
#     v1.draw()
#     return v1.end_point


# angle_0 = 90
# lenght_0 = 200
# next_point = branch(point=point_0, angle=90, lenght=100)
# next_angle =angle_0 - 30
# next_lenght = lenght_0 * 0.75
# next_point = branch(point=next_point, angle=next_angle, lenght=next_lenght)
# next_angle = next_angle - 30
# next_lenght = next_lenght * 0.75
# next_point = branch(point=next_point, angle=next_angle, lenght=next_lenght)

# написать цикл рисования ветвей с постоянным уменьшением длины на 25% и отклонением 30 градусов

angle_0 = 90
lenght_0 = 200

next_angle = angle_0
next_lenght = lenght_0
next_point = point_0

# while next_lenght > 10:
#     next_point = branch(point=next_point, angle=next_angle, lenght=next_lenght)
#     next_angle = next_angle - 30
#     next_lenght = next_lenght * 0.75

# сделать фукцию branch рекурсивной
def branch(point, angle, lenght, delta):
    if lenght < 1:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=lenght, width=3)
    v1.draw()
    next_point = v1.end_point
    next_angle = angle - delta
    next_lenght = lenght * 0.75
    branch(point=next_point, angle=next_angle, lenght=next_lenght, delta=delta)


for delta in range(0, 51, 10):
    branch(point=point_0, angle=90, lenght=100, delta=delta)
for delta in range(-50, 1, 10):
    branch(point=point_0, angle=90, lenght=100, delta=delta)


sd.pause()