# -----  Классы данных  ----------------------------------------------------------------------
from dataclasses import dataclass, field, InitVar
from pprint import pprint  # для вывода атрибутов классов данных


# простой метод создания класса данных
class ThingData1:
    # значения списка dims[] одни для все обьектов етого класса
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


# init = True  указывает что будет создаваться __init__ для екзепляров класса. Для реализации етого класса как базового для создания наследников
# repr = True  позволяет выводить свойства екзепляра етого класа через print
# eq = True    позволяет сравнивать екзпеляры етого красса между собой
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
    calc_len: InitVar[bool] = True

    # __post_init__ вызываеться после __init__ . Позволяет работать с екзпеляром класса данных после инициализации
    # Также добаляет функционал к екзеплярам обьекта класса
    def __post_init__(self, calc_len: bool):
        if calc_len:
            self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


a = Vector3D2(1, 2, 3)
b = Vector3D2(5, 7, 10)
print(a > b)
