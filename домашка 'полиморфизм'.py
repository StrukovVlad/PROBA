
"""
Описать абстрактный класс Transport:
- атрибут brand - фирма, выпустившая транспорт (тип - str)
- атрибут model - модель (тип - str)
- атрибут issue_year - год выпуска (тип - int)
- атрибут color - цвет (тип - str)
- атрибут mileage - пробег (тип - int)
- магический метод __init__, который принимает brand, model, issue_year и color,
  а mileage устанавливает значение 0
- абстрактный метод move, который принимает num_km - количество километров,
  которое должен пройти транспорт, проверяет, чтобы num_km было больше 0 и
  увеличивает mileage на значение num_km. Если num_km меньше 0, то бросить
  исключение ValueError("Расстояние должно быть положительным числом")
Описать класс Car, который наследуется от Transport:
- атрибут engine_type - тип двигателя (тип str)
- магический метод __init__, который принимает brand, model, issue_year и color
  и engine_type
- переопределить метод move. Внутри метода вызвать родительский метод, а потом
  вернуть строку "{brand} {model} ({color} - {issue_year}) проехала {km}
  километров"
Описать класс Airplane, который наследуется от Transport:
- атрибут lifting_capacity - грузоподъемность (тип - int)
- магический метод __init__, который принимает brand, model, issue_year и color
  и lifting_capacity
- переопределить метод move. Внутри метода вызвать родительский метод, а потом
  вернуть строку "{brand} {model} ({color} - {issue_year}) пролетел {km}
  километров"
"""
from abc import ABC, abstractmethod


class Transport(ABC):
    brand: str
    model: str
    issue_year: int
    color: str
    mileage: int

    def __init__(self, brand, model, issue_year, color):
        self.mileage = 0
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.color = color

    @abstractmethod
    def move(self, mileage, num: int):
        self.mileage = mileage
        if num > 0:
            self.mileage += num
        else:
            raise ValueError('Расстояние должно быть положительным числом')


class Car(Transport):
    engine_type: str

    def __init__(self, brand, model, issue_year, color, engine_type):
        super().__init__(brand, model, issue_year, color)
        self.engine_type = engine_type

    def move(self, mileage, num):
        super().move(mileage,num)
        return print(f'{self.brand} {self.model} ({self.color}-{self.issue_year}) проехала {self.mileage} км')


class Airplane(Transport):
    lifting_capacity: int

    def __init__(self, brand, model, issue_year, color, lifting_capacity):
        super().__init__(brand, model, issue_year, color)
        self.lifting_capacity = lifting_capacity

    def move(self, mileage, num):
        super().move(mileage, num)
        return print(f'{self.brand} {self.model} ({self.color}-{self.issue_year}) пролетела  {self.mileage} км')



Car('Renault','Megane',2017,'black','dizel').move(215000,14000)
Airplane('Boeing','747',2010,'silver',2.0).move(215000,14000)




"""
Описать абстрактный класс Device:
- определить абстрактный метод process_doc, который принимает аргумент name -
  название документа и будет бросать raise NotImplementedError
Описать класс Scanner, который наследуется от Device:
- переопределить метод process_doc, который будет возвращать строку
  "Сканирую документ: {name}"
Описать класс Copier, который наследуется от Device:
- переопределить метод process_doc, который будет возвращать строку
  "Делаю копию: {name}"
Описать класс MFU, который наследуется от Scanner и Copier:
- переопределить метод process_doc, который будет возвращать строку
  "Сканирую, отправляю факс: {name}"
В блоке if "__name__" == "__main__": создать объект класса MFU. Просмотреть MRO
"""


from abc import ABC, abstractmethod

class Device(ABC):
    name: str

    @abstractmethod
    def procecc_doc(self,name):
        self.name=name

class Scanner(Device):

    def procecc_doc(self,name):
        super().procecc_doc(name)
        return print(f'Сканирую документ: {self.name}')

class Copier(Device):

    def procecc_doc(self,name):
        super().procecc_doc(name)
        return print(f'Делаю копию : {self.name}')

class MFU(Scanner, Copier):

    def procecc_doc(self,name):
        super().procecc_doc(name)
        return print(f'Сканирую и отправляю факс :{self.name}')

a=MFU()
a.procecc_doc('строка')
print(MFU.mro())



"""
Создать 3 класса:
AmericanPerson, RussianPerson, GermanyPerson
в каждом классе определить метод i_love_science()
AmericanPerson.i_love_science() -> "I love science"
RussianPerson.i_love_science() - "Я люблю науку"
GermanyPerson.i_love_science() - "ich liebe Wissenschaft"
Написать функцию person_love_science, которая принимает объект и вызывает метод
i_love_science. Функция должна возвращать строку вида
"{obj.__class__.__name__} says that: {obj.i_love_science()}"
В блоке if __name__ == "__main__": сделать объекты трех классов и по очереди
передать их в функцию person_love_science.
https://www.youtube.com/watch?v=8o7ZKTvZpLc
"""

class AmericanPerson:
    def i_love_science(self):
        return 'I love science'


class RussianPerson:
    def i_love_science(self):
        return 'Я люблю науку'


class GermanyPerson:
    def i_love_science(self):
        return 'ich liebe Wissenschaft'


def person_love_science(obj):
    return f'{obj.__class__.__name__} says that: {obj.i_love_science()}'


if __name__ == "__main__":
    UA = AmericanPerson()
    RU = RussianPerson()
    GE = GermanyPerson()
    a = 3
    some_list = (UA, RU, GE)
    while a < 4:
        if not a == 0:
            a = a - 1
            print(person_love_science(some_list[a]))
        else:
            break



"""
Определить класс Person:
- атрибут fullname - ФИО (тип str)
- атрибут phone - номер телефона (тип str)
- магический метод __init__, который принимает fullname и phone
Описать класс LibraryReader, который наследуется от Person:
- атрибут uid - номер читательского билета (тип int)
- атрибут books - список книг (тип set)
- магический метод __init__, который принимает fullname, phone, uid, а books
  заполняет пустым множеством
- метод take_books(*args), который принимает произвольное количество книг
  (книга - строка с названием книги) и возвращает строку: "Петров В.В. взял(а)
  книги: Приключения, Словарь, Энциклопедия", если было взято до 3 книг
  включительно. Если было взято больше книг, то возвращает строку: "Петров В.В.
  взял(а) 4 книги".
- метод return_book(*args), который принимает произвольное количество книг
  (книга - строка с названием книги) и возвращает строку: "Петров В.В. вернул(а)
  книги: Приключения, Словарь, Энциклопедия", если было возвращено до 3 книг
  включительно. Если было возвращено больше книг, то возвращает строку:
  "Петров В.В. вернул(а) 4 книги". Если какой-то книги нет, то бросить исключение
  ValueError с сообщением "Петров В. В. не брал: Рассказы", при этом книги не
  должны быть удалены
Названия книг в сообщениях должны быть отсортированы по алфавиту.
"""

class Person:
    fullname: str
    phone: str

    def __init__(self, fullname, phone):
        self.fullname = fullname
        self.phone = phone


class LibraryReader(Person):
    uid: int
    books: set

    def __init__(self, fullname, phone, uid, books=None):
        super().__init__(fullname, phone)
        if books is None:
            books = set()
        self.uid = uid
        self.books = books

    def take_books(self, *args):
        self.books = self.books.union(args)
        if len(args) <= 3:
            args = list(args)
            args.sort()
            return f"{self.fullname} взял(а) книги: {', '.join(args)}"
        else:
            return f'{self.fullname} взял(а) {len(args)} книги'

    def return_book(self, *args):
        args = set(args)
        if self.books.issuperset(args):
            self.books = self.books.difference(args)
            if len(args) <= 3:
                lst = list(args)
                lst.sort()
                return f"{self.fullname} вернул(а) книги: {', '.join(lst)}"
            else:
                return f'{self.fullname} вернул(а) {len(args)} книги'
        else:
            raise ValueError(f'{self.fullname} не брал(а): {args.difference(self.books)}')