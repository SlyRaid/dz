# Цель работы
#   Более глубоко понять особенности работы с функциями генераторами и оператором yield в Python.
# Задание
#   Напишите функцию-генератор all_variants, которая будет возвращать все подпоследовательности переданной строки.
# В функцию передаётся только сама строка.
# Примечание
#   Используйте оператор yield

def all_variants(text: str):
    for start in range(0, len(text)):
        for end in range(start+1, len(text)+1):
            b = text[start:end]
            yield b

a = all_variants('abc')
for i in a:
    print(i)


# def all_variants(n):
#     yield ''
#     yield n[0]
#     yield n[1]
#     yield n[2]
#     yield n[0:2]
#     yield n[1:]
#     yield n
#
#
# a = all_variants("abc")
# for i in a:
#     print(i)

# import itertools
#
# def Sub_Sequences(STR):
# 	combs = []
# 	for l in range(1, len(STR)+1):
# 		combs.append(list(itertools.combinations(STR, l)))
# 	for c in combs:
# 		for t in c:
# 			yield (''.join(t))
#
#
# a = Sub_Sequences("abc")
# for i in a:
#     print(i)
