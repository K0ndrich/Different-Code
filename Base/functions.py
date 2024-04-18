# ----- Анотации Типов -------------------------------------------------------------------------------------------------------------------------------
# подсказка для програмиста, какой тип данных переменной принимает функция
def my_fn(a: int):
    pass


# анотация типа с указанием значения по умолчанию при отсуцтвии передачи агрумента
def my_fn(a: int = 10):
    pass


# ----- Явно указываем тип возвращаемого значения ----------------------------------------------------------------------
def my_fn(a, b) -> int:
    return a + b


# ----- Лямбда Функция ------------------------------------------------------------------------------------------------
# x     - ето аргумент
# x + 2 - ето возвращаемое значение
lambda x: x + 2


# ----- Тернарны Оператор ---------------------------------------------------------------------------------------------------
# выражение1 if условие else выражение2

a = 5 if 1 > 0 else 7


# ----- Рекурсия -----------------------------------------------------------------------------------------------------------------------------
# когда функция вызвает саму себя
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


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


# ----- *ARGS and **KWARGS -------------------------------------------------------------------------------------------------
# Большое количество аргументов передаеться по типу кортеж (tuple)
def my_fn(*args):
    return args  # возвращает [(1,2,3,4,5)]


#  Большое количество аргументов передаеться по типу словаря (dict)
def my_fn1(**kwargs):
    return kwargs  # возвращает {"key1":1 , "key2":2}


# ----- Функция MAP --------------------------------------------------------------------------------------------------------------
# map(name_function , my_list) -> map object
# применение указаной функции к каждому значению в последовательности
# возвращает все измененые значения в такой же последовательности
def my_fn_for_map(x):
    pass


map(my_fn_for_map, [1, 2, 3])
map(lambda x: x * 2, [1, 2, 3])
map(str.upper, ["name1", "name2"])

# возвращаемый обьект из map нужно преобразовывать в другой тип данных (list , set)
list(map(my_fn_for_map, [1, 2, 3]))


# ----- Функция FILTER -------------------------------------------------------------------------------------------------------
# filter(my_fn_for_filter or None , *iterables) -> filter object
# If inner function return True -> element go in filter object
# If selected None, as function None -> filter (None , [1,2,3]) == filter(bool , [1,2,3])
def my_fn_for_filter(x):
    if x > 10:
        return True
    else:
        return False


filter(my_fn_for_filter, [1, 2, 3])
filter(str.isdigit, [1, "hello", 2])
list(filter(my_fn_for_filter, [1, 2, 3]))


# ----- Функция ENUMERATE --------------------------------------------------------------------------------------------------------
# enumerate(*iterables) -> enum object
# Розделяет последовательность на пары кортежей по типу [ (0,10) , (1,20) , (2,30) , (3,40) ]
# , где первое число ендекс(index) значения, а второе и есть значение(value) последователньости
# enumerate([10,20,30,40] , my_value_index) можна указывать начальное значение индекса начало отсчета

list(enumerate([10, 20, 30, 40]))
# можно использовать цикл for
a = [10, 20, 30, 40]
b = {"key1": 1, "key2": 2}
for index, value in enumerate(range(11), 5):
    print(f"{index} --> {value}")

# -----   ZIP   ------------------------------------------------------------------------------------------------------------------------------------------
# zip позвоялет пройтись по нескольним последоватнельностям одновременно
# проходить по взятым последовательностям вертикально

a = [1, 2, 3]
b = [4, 5, 6, 7]
c = [8, 9]
for x in zip(a, b, c):
    print(x)

# результатом возвращает пари из кортежей
# (1, 4, 8)
# (2, 5, 9)
