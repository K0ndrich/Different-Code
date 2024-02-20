# ----- Вычесляем часы , минуты и секунды по указанию количества секунд -------------------------------
# ----- Можно добавлять значения к обьекту или другие обьекты, сравнивать обьекты между собой ----------------------------------------------------


class Clock:
    __DAY = 86400  # количество секунд в дне

    # инициализатор
    def __init__(self, seconds: int):

        if not isinstance(seconds, int):
            raise TypeError("ERROR")
        self.seconds = seconds % self.__DAY

    # геттер
    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"h - {self.__get_formatted__(h)} , m - {self.__get_formatted__(m)} , s - {self.__get_formatted__(s)}"

    # метод класса -> создан для работы только внутри класса
    @classmethod
    def __get_formatted__(cls, x):
        return str(x).rjust(2, "0")

    # добавление типа my_object + 10
    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("ERROR")

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        return Clock(self.seconds + sc)

    # добавление типа 10 + my_object
    def __radd__(self, other):
        return self + other

    # добавление типа my_object += 10
    def __iadd__(self, other):

        if not isinstance(other, (int, Clock)):
            raise TypeError("ERROR")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        self.seconds += sc
        return self

    # проверка принимаемых значений для сравнений
    @classmethod
    def __verify_data(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("ERROR")
        return other if isinstance(other, int) else other.seconds  # тернарный оператор

    # вызов оператора равенства == . Если оператор неравенства != тогда not (my_object1 == my_object2)
    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.seconds == sc

    # вызов оператора меньше < . Если оператор больше > , тогда меняем местами обьекты my_object2 < my_object1
    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds < sc

    # вызов оператора меньше или равно <= . Если оператор больше или равно >= , тогда меняем метсами my_object2 >= my_object1
    def __le__(self, other):
        sc = self.__verify_data(other)
        return self.seconds <= sc


# ----- Множетсвенное Наследование + Миксины -> Магазин с техникой ---------------------------------------------------
class Goods:
    def __init__(self, name, weight, price):
        super().__init__(1)  # подключаем миксин, создаеться екзепляр класса MixinLog
        print(" ---- init  GOODS -----")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name} - {self.weight} - {self.price}")


class MixinLog:  # создание миксина
    ID = 0

    def __init__(self, p1):
        print(" ----- init - MIXIN LOG -------")
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f"{self.id} - product was been sale")


# при вызове методы, он ищетсья сначала 1. Notebook -> потом 2. Goods -> потом MixinLog
class NoteBook(Goods, MixinLog):
    pass

