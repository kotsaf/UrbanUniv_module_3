#Задача "Распаковка"
#Пункт 1
def print_params(a = 1, b = 2, c = 3):
    print(a, b, c)

print_params()
print_params(a = 3)
print_params(1, 25, 3)
print_params(1, 2, c = [1,2,3])

#Пункт 2
values_list = [1, 'Str', 3.22]
values_dict = {'a': 'edsw', 'b': 9.8, 'c': True }

print_params(*values_list)
print_params(**values_dict)

#Пункт 3
values_list_2 = [False, 6]
print_params(*values_list_2, 42)