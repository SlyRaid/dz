def triple(x=1, y=2, z=3):
    print(x, y, z)


def triple2(x='A', y='B', z='C'):
    print(x, y, z)


listok = [2, 3, 4]


def triple3(x, y, z):
    print(x, y, z)


triple(x=2)
triple2()
triple3(*listok)
