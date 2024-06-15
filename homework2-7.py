def print_params(a = 1, b = 'строка', c = True):
    print_params() # Принта не будет, поскольку не заданы параметры
    print_params(a)  # Принта не будет, поскольку не заданы все параметры
    print_params(b=25) # Принта не будет, поскольку меняем разные типы данных
    print_params(c=[1, 2, 3]) # Принта не будет, поскольку меняем разные типы данных

values_list = [15, 'слово', False]
values_dict = {'a': 10, 'b': "яблоко", 'c': 4.5}
print_params(*values_list) # Выдает ошибку "Превышена максимальная глубина рекурсии"
print_params(**values_dict) # Такая же ошибка

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42) # Такая же ошибка, как и выше
