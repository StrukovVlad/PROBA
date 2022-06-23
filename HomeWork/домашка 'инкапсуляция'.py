"""
Создать класс BookCard, в классе должны быть:
- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).
Аксессоры реализоваться через property.
"""

from datetime import date

CURRENT_YEAR = date.today().year


class BookCard:
    __author: str
    __title: str
    __year: int

    def __init__(self, __author, __title, __year):
        self.__author = __author
        self.__title = __title
        self.__year = __year

    def sorting_book(self):
        pass

    @property
    def get_author(self):
        return self.__author

    @get_author.setter
    def get_author(self, new_author):
        if isinstance(new_author, str):
            self.__author = new_author
        else:
            raise ValueError("Не верное значение.")

    @property
    def get_title(self):
        return self.__title

    @get_title.setter
    def get_title(self, new_title):
        if isinstance(new_title, str):
            self.__title = new_title
        else:
            raise ValueError("Не верное значение.")

    @property
    def get_year(self):
        return self.__year

    @get_year.setter
    def get_year(self, new_year):
        if isinstance(self.__year, int):
            if 0 < new_year <= CURRENT_YEAR:
                self.__year = new_year
            elif new_year <= 0:
                raise ValueError("Мы не храним книг, изданных до нашей эры.")
            else:
                raise ValueError("Мы не храним книги из будущего.")
BookCard('Read','1925',1910).get_title()

"""
Напишите класс GameObject, в котором будут храниться координаты объекта.
- private атрибут x (тип int)
- private атрибут y (тип int)
- магический метод __init__, который принимает начальные x и y
Координаты должны быть доступны для чтения (сделать property), а их изменение
должно происходить в методе move(delta_x, delta_y). (изменение - это +=)
"""


class GameObject:
    __x: int
    __y: int

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def move(self, delta_x, delta_y):
        self.__x += delta_x
        self.__y += delta_y

