# ----- Call Back Функции ------------------------------------------------------------------------------------------


def my_fn1(func):

    func()


def my_call_back_func():  # my_fn2 - ето call back функция.
    pass  # Ета функция передаеться внутрь другой функции, как аргумент


my_fn1(my_call_back_func)

# ----- Функции Замыкания -----------------------------------------------------------------------------------------


def my_fn1(value):

    def my_lock_func():  # my_fn2 - ето функция замыкания.
        pass  # Ета функция реальзована внутри другой функции и возвращаеться из внешней функции

    return my_lock_func


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


# -----   Дескрипторы   ------------------------------------------------------------------------------------------------
class MyDescriptor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        # или  return getattr( instance , self.name)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        # или  setattr( instance, self.name , value)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print("---- DELETED ----")
        del self.name


class OtherMyDescriptor:
    x = MyDescriptor()
    y = MyDescriptor()

    def __init__(self, x, y):
        self.x = x
        self.y = y


# ----- Миксины -> Множетсвенное Наследование ----------------------------------------------------------------


class FirstClass:
    def __init__(self):
        super().__init__()  # создание екзепляра класса Mixin и поключение его


class Mixin:
    # внутри инициализации __init__  миксина нельзя указывать параметры
    def __init__():
        pass


class SecondClass(FirstClass, Mixin):
    pass


# ----- Магические Методы для работы с Списками ---------------------------------------------------------------------------------


class List:
    def __init__(self, marks):
        self.marks = list(marks)

    # возвращает елемент через обращение [ ]
    def __getitem__(self, item):
        if 0 <= item <= len(self.marks):
            return self.marks[item]

    # записываем новый елемент через a[3] = "abc", если список мал тогда розширяем
    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("ERROR")
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)
        self.marks[key] = value

    # удаление елемента списка по ключу
    def __delitem__(self, key):
        if not isinstance(key, int) or key >= len(self.marks):
            raise TypeError("ERROR")
        del self.marks[key]


# ----- Магические методы для работы с Циклами ----------------------------------------------------------------


class Cycle:
    def __init__(self, start=0.0, step=0.0, stop=0.0):
        self.start = start
        self.step = step
        self.stop = stop

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration

    def __iter__(self):
        self.value = self.start - self.step
        return self


# Создание таблици из списков
class Cycle2D:
    def __init__(self, start=0.0, step=0.0, stop=0.0, rows=5):
        self.rows = rows
        self.fr = Cycle(start, step, stop)

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration

    def get_info(self):
        for row in self:
            print("------------------")
            for y in row:
                print(y, end=" ")
            print(sep="\n")
