from time import sleep
from threading import Thread


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
alfavit = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def sec1(name):
    for i in name:
        print(i, flush=True)
        sleep(1)

th = Thread(target=sec1, kwargs=dict(name=numbers))
th.start()

sec1(name=alfavit)

th.join()


