# -----   Методы Класса   -------------------------------------------------------------------------------------------------------------------------------
# можно работать только с полями и методами класса , работать с полями екзепляра не можна


class MyClass:
    my_var = 1

    @classmethod
    def my_fn(cls):
        return cls.my_var


# -----   Статические Методы   ----------------------------------------------------------------------------------------------------------------------------------------
# не можно работать с полями ни класса, ни екзепляра


class MyClass:

    @staticmethod
    def my_fn():
        return 2 + 2


# -----   @property    .setter   .deleter    -------------------------------------------------------------------------------------------------------------------------
# позволяет создавать, изменять и удалять динамические атрибуты


class Person:
    first_name: str
    last_name: str

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, value):
        name_surname = value.split(" ")
        self.first_name = name_surname[0]
        self.last_name = name_surname[1]

    @full_name.deleter
    def full_name(self):
        del self.first_name
        del self.last_name


a = Person("Max", "Kondrich")
a.full_name = "Sana Olegov"
del a.full_name


# -----   Модификаторы Доступа   ------------------------------------------------------------------------------------------------------------------------------------------------------
# только оповищают програмиста и не изменяют функционал


class MyClass:
    # a - установлен модификтор public
    # может обращается текущий класс, наследники класса и обьекты
    a = 3

    # _a - установлен модификатор protected
    # может обращатся текущий класс и классы наследники
    _a = 5

    # __a - установлени модификатор private
    # может обращаться только текущий класс
    __a = 7


my_object = MyClass()
# print(my_object.a)
# print(my_object._a)
# print(my_object._MyClass__a)

# -----   Миксины    -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# добавялет свойства и методы для класса, который будет наследовать миксин
# миксин при наследовании пишесть самым последним, чтом значение миксина не изменилось
# множественное наследование идет слева на право


class Mixin:
    a = 3


class MyClass(Mixin):
    a = 5


class MySecondClass(MyClass, Mixin):
    a = 7

# -----   Композиция   -------------------------------------------------------------------------------------------------------------------------------------

class MyClass():
    pass

class SecondClass():
    a = MyClass()


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


# -----   Абстрактный Классы , Абстрактные Методы   --------------------------------------------------------------------------------------------------------------------------
import abc


# создание абстрактного класса
class AbstractClass(abc.ABC):
    # создание абстрактного методы
    # етот метод нужно переопределяться в классе наследнике
    @abc.abstractmethod
    def my_fn(self):
        raise NotImplemented


class MyClass(AbstractClass):
    def my_fn(self):
        print("hello")


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


# -----   __new__  ->  __init__   --------------------------------------------------------------------------------------------------------------


class MyClass:
    # метод создает обьект
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        return obj

    # метод иницализирует обьект , который передаеться от __new__
    def __init__(self):
        self.a = 1


# -----   super   ----------------------------------------------------------------------------------------------------------------------------------------
# служит для обращения к методам родительского класса, от которого наследуем текущий


class MyClass:
    def __init__(self):
        # print("hello")
        pass


class MySecondClass(MyClass):

    def __init__(self):
        super().__init__()


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


# создание класса через мета функцию. В екзепляре етого класса не будет локальных свойств
class Point1(metaclass=create_class_point):
    def get_coords(self):
        return (0, 0)


# созданий пользовательский метакласс из главного метакласса type()
class Meta(type):
    def __new__(cls, name, base, attrs):
        attrs.update({"MAX_CORD": 100, "MIN_CORD": 0})
        return type.__new__(cls, name, base, attrs)


# создание класса через пользовательский метакласс. В екзепляре етого класса не будет локальных свойств
class Point2(metaclass=Meta):
    def get_coords(self):
        return (0, 0)


# ----- Класс Women был создан по мета классу Meta. При создании екзепляря класса Women уже есть свойства с значениями ---------------------------------------------------------


class Meta(type):
    def create_local_attrs(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

    def __init__(cls, name, bases, attrs):
        cls.class_attrs = attrs
        # добавляет инициализотор для класса Women
        cls.__init__ = Meta.create_local_attrs


# екзепляри етого класса будуть иметь локальные свойства указаные ниже
class Women(metaclass=Meta):
    title = "123_title"
    content = "123_content"
    photo = "123_photo"
