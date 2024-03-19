
import simple_draw as sd

sd.resolution = (1200, 600)
# познакомится с параметрами библеотечной функции рисования снежинки sd.snowflake()

point_0 = sd.get_point(100, 500)
sd.snowflake(center=point_0, length=200)

# реализовать падение одной снежинки

while True:
    for x in range(1, 501, 50):
        for y in range(500, 0, 50):
            sd.clear_screen()
            point = sd.get_point(x, y)
            sd.snowflake(center=point, length=50)
            y -= 10
            if y < 50:
                break
            x *= 1.1
            sd.sleep(0.1)
            if sd.user_want_exit():
                break


# реализовать падение одной снежинки из произвольного места экрана

# реализовать падение одной снежинки с ветром - смещение в сторону


sd.pause()