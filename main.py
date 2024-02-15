# -----   Патерн Singleton -> Создаеться только один екзепляр класса  -----------------------------------------------------------------------------------------
class MySigleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(MySigleton, cls).__new__(cls)
        return cls.instance

    def __init__(self, x, y):
        self.x = x
        self.y = y


# -----   Патерн Моносостояние -> Свойства для всех екзепляров класса одинковые --------------------------------------------------------------------------------------
class MyMonoCondition:
    __data = {"name": "", "age": 0, "city": ""}

    def __init__(self):
        self.__dict__ = self.__data


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


# ----- Вычесляем часы , минуты и секунды по указанию количества секунд -------------------------------
# ----- Можно добавлять значения к обьекту или другие обьекты, сравнивать обьекты между собой ----------------------------------------------------


class Clock:
    __DAY = 86400  # количество секунд в дне

    # инициализатор
    def __init__(self, seconds: int):

        if not isinstance(seconds, int):
            raise TypeError(" --- eror ---")
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
