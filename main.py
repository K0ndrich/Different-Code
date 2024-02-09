# -----  Декораторы  ------------------------------------------------------------------------------------------------
class Integer:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Point3D:
    x = Integer()
    y = Integer()

    def __init__(self, x, y):
        self.x = x
        self.y = y


a = Point3D(1, 2)
print(a.x)
