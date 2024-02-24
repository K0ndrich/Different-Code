# -----  Классы данных  ----------------------------------------------------------------------
from dataclasses import dataclass, field, InitVar
from pprint import pprint  # для вывода атрибутов классов данных
from typing import Any  # анотация типов , Any - ето означает любой тип данных


# простой метод создания класса данных
class ThingData1:
    # значения списка dims[] одни  для все обьектов етого класса
    def __init__(self, name, weight: int = 0, price: int = 0, dims: list = []):
        self.name = name
        self.weight = weight
        self.price = price
        self.dims = dims

    # методы вывода данных в print или str
    def __repr__(self):
        return f"class Thing{self.__dict__}"


#  Класс ThingData1 равносилен классу ThingData2  (ThingData1 == ThingData2)


@dataclass
class ThingData2:
    # без указания типа декоратора dataclass не добавит в екзпеляри обьекта данное поле
    name: str
    # можно указывать значения по умолчанию
    weight: int = 1
    # значения по умолчанию можно указывать всегда последними , после них без умолчанию указывать нельзя
    price: float = 0
    # нельзя присваивать атрибутам обьектам изменяемые типы данных просто так (вот так нельзя ->)
    dims: list = []
    # через ключевое слово field можно присваивать изменяемые типы
    # default_factory = при создании начиванет ссылаться на пустой список
    dims: list = field(default_factory=list)

    def __eq__(self, other):
        return self.weight == other.weight


# сравниваються значения обьектов , а не их индетификаторы
# print(a == b)     или    my_object1 (name , weight , price ) == my_object2 (name , weight , price )
# pprint(ThingData2.__dict__)  # выводит атрибути которые содержит сторонний класс данных


# ----- Добавление функционала для классов данных -----------------------------------------------------------------------


class Vector3D1:
    def __init__(self, x: int, y: int, z: int, calc_len: bool = True):
        self.x = x
        self.y = y
        self.z = z
        self.length = (x * x + y * y + z * z) ** 0.5 if calc_len else 0


#  Класс Vector3D1 равносилен классу Vector3D2  (Vector3D1 == Vector3D2)


# init = True   указывает что будет создаваться __init__ для екзепляров класса. Для реализации етого класса как базового для создания наследников
# repr = True   позволяет выводить свойства екзепляра етого класа через print
# eq = True     позволяет проверять на равенство екзпеляры етого класса между собой ==  !=
# order = True  позволяет сравнивать екзепляри етого класса через > >= <= <=. Рабатет вместе с eq = True + order = True
# frozen = True разрешает изменять значения локальных свойств екзепляра етого класса
@dataclass(eq=True)
class Vector3D2:
    # repr = False указывает что ето свойство не будет выводиться при print()
    x: int = field(repr=False)
    # copmare = False указывает что свойство не будет учитываться при сравнении обьектов через ==
    y: int = field(compare=False)
    # default = 0 указывает значение по умолчанию
    z: int = field(default=0)
    #  init = False не добавляет указаное свойство в инициализатор __init__ как параметр поетому уже может выводиться как локальное свойство
    length: float = field(init=False, compare=False, default=0)
    # свойство автоматически передаеться как аргумент в __post_init__ , по умолчанию свойтво имеет значение True и принимает только bool
    # свойство не добавляеться в сравнение между екзеплярами класса
    calc_len: InitVar[bool] = True

    # __post_init__ вызываеться после __init__ . Позволяет работать с екзпеляром класса данных после инициализации
    # Также добаляет функционал к екзеплярам обьекта класса
    def __post_init__(self, calc_len: bool):
        if calc_len:
            self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


# ----- Наследование Классов Данных  -----------------------------------------------------------------------------


class GoodsMethodFactory:
    @staticmethod
    def get_init_measure():
        return [0, 0, 0]


@dataclass
class Goods:
    # current_uid ето свойство только класса Goods. В наследниках или екзеплярах его не будет
    # ето уникальный id для каждогого екзепляра етого класса или классов наследников
    current_uid = 0
    uid: int = field(init=False)
    price: Any = 0
    weight: Any = 0

    def __post_init__(self):
        Goods.current_uid += 1
        self.uid = Goods.current_uid


@dataclass
class Book(Goods):
    # в класе наследнике переопределяються свойства от базового класса
    title: str = ""
    author: str = ""
    price: float = 0
    weight: int | float = 0

    @staticmethod
    def get_init_measures():
        return [0, 0, 0]

    # свойство оперделяеться методом, который реализован в классе више
    # в свойстве храниться список из трех елементов , по умолчанию [ 0 , 0 , 0 ]
    measure: list = field(default_factory=Book.get_init_measures)

    def __post_init__(self):
        super().__post_init__()


a = Book(10, 100, "max", "kondrich")
a1 = Book(10, 100, "max", "kondrich")
a2 = Book(10, 100, "max", "kondrich")
a3 = Book(10, 100, "max", "kondrich")
a4 = Book(10, 100, "max", "kondrich")
a5 = Book(10, 100, "max", "kondrich")
print(a5.measure)
