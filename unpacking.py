def print_params(a=1, b='строка', c=True):
    return print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [5, "word", True]
values_dict = {'a': 9, 'b': "world", 'c': False}
print_params(*values_list)
print_params(**values_dict)

