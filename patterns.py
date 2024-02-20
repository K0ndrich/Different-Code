# -----   Патерн Singleton -> Создаеться только один екзепляр класса  -----------------------------------------------------------------------------------------
class MySigleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(MySigleton, cls).__new__(cls)
        return cls.instance

    def __init__(self, x, y):
        self.x = x
        self.y = y


# -----   Патерн Моносостояние -> Свойства для всех екзепляров класса одинковые. Екзепляры имеють одни значения свойст на всех --------------------------------------------------------------------------------------
class MyMonoCondition:
    __data = {"name": "", "age": 0, "city": ""}

    def __init__(self):
        self.__dict__ = self.__data
