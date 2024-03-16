# ------ Call Back Функции --------------------------------------------------------------------------------------
def my_fn1(my_fn2):

    my_fn2()


def my_fn2():  # my_fn2 - ето call back функция.
    pass  # Ета функция передаеться внутрь другой функции, как аргумент


my_fn1(my_fn2)

# ----- Функции Замыкания -----------------------------------------------------------------------------------------


def my_fn1(value):

    def my_fn2(value):  # my_fn2 - ето функция замыкания.
        pass  # Ета функция реальзована внутри другой функции и возвращаеться из внешней функции

    return my_fn2


a = my_fn1(777)

# ----- Декораторы Функций -------------------------------------------------------------------------------------------------


def my_decorator_func(func):
    def wrapper(value):
        func(value)

    return wrapper


@my_decorator_func  # первый способ добавление декоратора
def my_fn():
    pass


my_fn = my_decorator_func(my_fn)  # второй способ добавления декоратора


# явно указываем тип возвращаемого значения
def my_fn(a, b) -> int:
    return a + b


# Большое количество аргументов передаеться по типу кортеж (tuple)
def my_fn(*args):
    return args  # возвращает [(1,2,3,4,5)]


#  Большое количество аргументов передаеться по типу словаря (dict)
def my_fn1(**kwargs):
    return kwargs  # возвращает {"key1":1 , "key2":2}


# Функция MAP
# map(name_function , *iterables) -> map object
def my_fn_for_map():
    pass


map(my_fn_for_map, [1, 2, 3])


# Функция FILTER
# filter(my_fn_for_filter , *iterables) -> filter object
# If inner function return True element go in filter object
def my_fn_for_filter(x):
    if x > 10:
        return True
    else:
        return False


filter(my_fn_for_filter, [1, 2, 3])
