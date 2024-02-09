# -----  Патерн Singleton  -----------------------------------------------------------------------------------------
class MySigleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(MySigleton, cls).__new__(cls)
        return cls.instance

    def __init__(self, x, y):
        self.x = x
        self.y = y


# -----  Патерн Моносостояние  --------------------------------------------------------------------------------------
class MyMonoCondition:
    __data = {"name": "", "age": 0, "city": ""}

    def __init__ (self):
        self.__dict__= self.__data


# -----  Декораторы  ------------------------------------------------------------------------------------------------
class MyDecorator:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class OtherMyDecorator:
    x = MyDecorator()
    y = MyDecorator()

    def __init__(self, x, y):
        self.x = x
        self.y = y
