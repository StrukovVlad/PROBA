"""
Описать абстрактный класс Shape - фигура, у которого:
- абстрактный метод get_perimeter (не принимает аргументов) для расчета периметра
- абстрактный метод get_square (не принимает аргументов) для расчета площади
Во всех дочерних классах методы get_perimeter и get_square должны возвращать
результат вычислений.
Описать класс Circle для круга (дочерний класс для Shape), у которого:
- атрибут r - радиус, тип float
- магический метод __init__, который принимает r
- перегрузить метод get_perimeter (формула длины окружности: 2 * pi * r)
- перегрузить метод get_square (формула площади: pi * r ** 2)
Описать класс Rectangle для прямоугольника (дочерний класс для Shape), у которого:
- атрибут a - первая сторона, тип float
- атрибут b - вторая сторона, тип float
- магический метод __init__, который принимает a и b
- перегрузить метод get_perimeter (формула периметра: 2 * (a + b))
- перегрузить метод get_square (формула площади: a * b)
Описать класс Square для квадрата (дочерний класс для Rectangle), у которого:
- магический метод __init__, который принимает a, вызывает super
"""


class Shape (ABC):

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_square(self):
        pass


class Circle(Shape):
    r: float

    def __init__(self, r):
        self.r = r

    def get_perimeter(self):
        b = 2 * pi * self.r
        return b

    def get_square(self):
        c = pi * self.r ** 2
        return c


class Rectangle(Shape):
    a: float
    b: float

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_perimeter(self):
        p = 2 * (self.a + self.b)
        return p

    def get_square(self):
        s = self.a * self.b
        return s


class Square(Rectangle):
    def __init__(self, a):
        super(Square, self).__init__(a, b=a)


"""
Описать абстрактный класс Animal у которого:
- атрибут name - кличка (тип str)
- магический метод __init__, который принимает аргумент name
- абстрактный метод says, который не принимает аргументов
На основе Animal определить классы Cat, Dog, Cow, которые переопределят метод
says таким образом, чтобы он возвращал строку вида:
- "{кличка} - кошка. Говорит МЯУ!" для класса Cat
- "{кличка} - собака. Говорит ГАВ!" для класса Dog
- "{кличка} - корова. Говорит МУ!" для класса Cow
"""


from abc import ABC , abstractmethod

class Animal(ABC):
    name: str
    def __init__(self,name):
        self.name=name

    @abstractmethod
    def says(self):
        return('ok')

class Cat(Animal):
    def says(self):
        super().says()
        return (f'{self.name} -кошка. Говорит  МЯУ!')

class Dog(Animal):
    def says(self):
        super().says()
        return (f'{self.name} -собака.Говорит ГАВ!')

class Cow(Animal):
    def says(self):
        super().says()
        return (f'{self.name} -корова.Говорит МУУ!')

name='Маруся'
a=(Cat(name),Dog(name),Cow(name))
for tex in a:
    print(tex.says())



