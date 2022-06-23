"""
Описать класс Counter, реализующий целочисленный счетчик.
который может увеличивать или уменьшать свое значение (атрибут value)
на единицу в заданном диапазоне.

Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.

Определить атрибуты:

- value - текущее значение счетчика

Определить методы:

- инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
- increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
- decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
- метод __iter__
- метод __next__
"""
class Counter:
    value: int

    def __init__(self, value=0):
        self.value = value

    def increase(self, num=1):
        self.value += num
        return self.value

    def decrease(self, num=1):
        self.value -= num
        return self.value

    def __iter__(self):
        return self

    def __next__(self):
        number = self.value
        self.value += 1
        return number



"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""
class Phone:

    def __init__(self, brand, model, year, name):
        self.brand = brand
        self.model = model
        self.year = year
        self.name = name

    def receive_call(self):
        return print(f' Звонит {self.name}')

    def get_info(self):
        return print(self.brand, self.model, self.year)

    def __str__(self):
        return print(f'Брэнд : {self.brand}\n',
                     f'Марка : {self.model}\n',
                     f'Год выпуска : {self.year}')

brand = input('Введите марку бренда:')
model = input('Введите марку модели :')
year = input('Введите год выпуска :')
name = input('Ваше имя :')
z = Phone(brand, model, year, name)
z.receive_call()
z.get_info()
a = z.__str__()

"""
Написать функцию hello, которая принимает аргумент name - строку с именем и
выводит принтом "Привет, {name}"

Написать декоратор log_decorator, который перед выполнением
функции печатает на экран строку, вида
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}".
После выполнения функции напечатать строку "Выполнено {func.__name__}"
"""
def log_decorator(func):
    def wrapper(*args,**kwargs):
        print(f'Выполняем {func.__name__} с args:{args} и с kwargs:{kwargs}')
        rezult=func(*args,**kwargs)
        print(f'Выполнено {func.__name__}')
        return rezult
    return wrapper

@log_decorator
def hello(name: str):
    print( f'Привет, {name} !')

z=input("Введите имя:")
hello(z)

"""
Написать замыкание.

Написать функцию add_numb, которая должна принимать некоторое целое число.
Написать внутри функции add_numb функцию inner, которая также принимает
целое число и возвращает сумму чисел, которое принимает она и которое
принимает функция add_numb.

Пример:
add_two = add_numb(2)
add_two(3)  # 5

add_three = add_numb(3)
add_three(3) # 6
"""
def add_number(x):
    def inner(y):
        return x+y
    return inner
a=add_number(1)(3)
print(a)

"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.

Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").
Проверить, что все аргументы целые можно с помощью функции all:
https://pyneng.readthedocs.io/ru/latest/book/10_useful_functions/all_any.html

Если все аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
слова должны быть строками").

Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""
def dict_from_args(*args,**kwargs):
    if all(type(a)==int for a in args):
        n=sum(args)
    else:
        raise TypeError('Все позиционные аргументы должны быть целыми')
    if all(type(b)==str for b in kwargs.values()):
        maxlenght=max(len(b) for b in kwargs.values())
    else:
        raise TypeError('Все аргументы -ключевые слова должны быть строками')
    return {'args_sum':n,'kwargs_max_len':maxlenght}

"""
Написать генератор get_even_number, который возвращает подряд четные числа

Например:

even_gen = get_even_number()

next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""
def get_even_number():
    a=range(2,100,2)
    for i in a:
        yield i
print(next(get_even_number()))
print(next(get_even_number()))
print(next(get_even_number()))
print(next(get_even_number()))
print(next(get_even_number()))
print(next(get_even_number()))

"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""
def fibonacci():
    a,b=0,1
    for i in range(0,100):
        a,b=b,a+b
        yield a
fibonacci_gen=fibonacci()
print(next(fibonacci_gen))

"""
Написать генератор fibonacci, который возвращает подряд значения числе Фибоначчи

Например:

fibonacci_gen = fibonacci()

next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 2
next(fibonacci_gen) -> 3
next(fibonacci_gen) -> 5
next(fibonacci_gen) -> 8
"""

def fibonacci():
    a,b = 0, 1
    for i in range(0, 100):
        a, b = b, a + b
        yield a
fibonacci_gen=fibonacci()
print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))

"""
Написать генератор triangular_numbers, который возвращает подряд числа
треугольные числа


Формула:
Tn = 1 / 2 * n * (n + 1)


Например:
tn_gen = triangular_numbers()

next(tn_gen) -> 1
next(tn_gen) -> 3
next(tn_gen) -> 6
next(tn_gen) -> 10
next(tn_gen) -> 15
next(tn_gen) -> 21
"""

def triangular_numbers():
    for i in range(1, 100):
        z = 1/2 * i * (i+1)
        yield z
tn_gen=triangular_numbers()
print(next(tn_gen))
print(next(tn_gen))
