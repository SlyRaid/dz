import simple_draw as sd
# нарисовать треугольник из точки (300, 300) с длиной 200
length = 200
point = sd.get_point(300, 300)

# v1 = sd.get_vector(start_point=point, angle=0, length=200, width=3)
# v1.draw()
#
# v2 = sd.get_vector(start_point=v1.end_point, angle=120, length=200, width=3)
# v2.draw()
#
# v3 = sd.get_vector(start_point=v2.end_point, angle=240, length=200, width=3)
# v3.draw()

def triangle(point, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=200, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=200, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=200, width=3)
    v3.draw()

point_0 = sd.get_point(300, 300)

for angel in range(0, 360, 30):
    triangle(point=point_0, angle=angel)

sd.pause()