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


# -----   Дескрипторы  -> Вписываються внутрь других классов, чтоб для каждого класса не прописывать геттери и сеттеры ------------------------------------------------------------------------------------------------
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


# ----- Магические методы для работы с менеджером контекста ( with )  -------------------------------------------------------


class DefenderVector:
    def __init__(self, vector):
        self.__vector = vector

    # метод вызываеться при создании менеджера контекста with
    def __enter__(self):
        self.__temp = self.__vector[:]
        return self.__temp

    # методы вызываетсья при когда завершиласть работа с файлом
    # в exc_type передаеться None если Exceptions не возникло
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__vector[:] = self.__temp
        # возвращаем False -> значить исключения , котоые возникли внутри менеджера контекста обрабатываться не будут и выходить за менеджер тоже не будут
        return False


vector1 = [1, 2, 3]
vector2 = [4, 5, 2]

try:
    # a = self.__temp , dv ссылаеться на копию списка vector1
    # к vector1 при бавляються значения по ндексу из vector2
    with DefenderVector(vector1) as a:
        for index, value in enumerate(a):
            a[index] += vector2[index]
except:
    print("")

# ----- Вложение классы --------------------------------------------------------------
# Класс для абстрактной базы данных


class People:
    title = "name_title"
    photo = "name_photo"
    ordering = "name_id"

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        self.meta = self.Meta(user + "@" + psw)

    # создает идентификатор для каждой строки в базе данных
    class Meta:
        def __init__(self, access):
            self.__access = access


# ----- Метакласс -> только type () ------------------------------------------------------------------------------------


class B1:
    pass


class B2:
    pass


def method1(self):
    print(self.__dict__)


# создание класса через мета класс type()
a = type(
    "Point",
    (B1, B2),
    {"MAX_CORD": 100, "MIN_CORD": 0, "method1": lambda self: print(self.MAX_CORD)},
)


# ----- Пользовательские метакласс и метафункции для создания других классов --------------------------------------------------
# создание мета функции для создания класса из главного метакласса type()
def create_class_point(name, base, attrs):
    attrs.update({"MAX_CORD": 100, "MIN_CORD": 0})
    return type(name, base, attrs)


# создание класса через мета функцию
class Point1(metaclass=create_class_point):
    def get_coords(self):
        return (0, 0)


# созданий пользовательский метакласс из главного метакласса type()
class Meta(type):
    def __new__(cls, name, base, attrs):
        attrs.update({"MAX_CORD": 100, "MIN_CORD": 0})
        return type.__new__(cls, name, base, attrs)


# создание класса через пользовательский метакласс
class Point2(metaclass=Meta):
    def get_coords(self):
        return (0, 0)
