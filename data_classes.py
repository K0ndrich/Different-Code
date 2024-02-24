# -----  Классы данных  ----------------------------------------------------------------------
from dataclasses import dataclass, field
from pprint import pprint  # для вывода атрибутов классов данных


# декоратор делает етот класс -> классов данных
@dataclass
class ThingData1:
    name: str
    # можно указывать значения по умолчанию
    weight: int = 1
    # значения по умолчанию можно указывать всегда последними , после них без умолчанию указывать нельзя
    price: float = 0
    # нельзя присваивать атрибутам обьектам изменяемые типы данных просто так
    dims: list = []
    # через ключевое слово field можно присваивать изменяемые типы
    # default_factory = при создании начиванет ссылаться на пустой список
    dims: list = field(default_factory=list)

    def __eq__(self, other):
        return self.weight == other.weight


# класс данных будет равносильно записи  ==  --->


class ThingData2:
    # значения списка dims[] один для все обьектов етого класса
    def __init__(self, name, weight=1, price=0, dims=[]):
        self.name = name
        self.weight = weight
        self.price = price
        self.dims = dims

    # методы вывода данных в print или str
    def __repr__(self):
        return f"class Thing{self.__dict__}"


# сравниваються значения обьектов , а не их индетификаторы
# print(a == b)     или    my_object1 (name , weight , price ) == my_object2 (name , weight , price )
# pprint(ThingData1.__dict__)  # выводит атрибути которые содержит сторонний класс данных
