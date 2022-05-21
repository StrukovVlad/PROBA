"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция decr_students, которая принимает SCHOOL_DATA, название класса и
    уменьшает количество учеников на 1, но не меньше 0
- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
- Функция remove_class, которая принимает SCHOOL_DATA, название класса и удаляет
    класс из словаря
- Функция calc_students, которая принимает SCHOOL_DATA и возвращает кол-во
    учеников во всей школе
"""
school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}
def incr_students(school_data,name):
    if name in school_data:
        school_data[name]+=1
        return school_data[name]
incr_students(school_data,'1a')
print(school_data)

def decr_students(school_data,name):
    if name in school_data:
        school_data[name]-=1
        return school_data[name]
decr_students(school_data,'1a')
print(school_data)

def add_class(school_data,name):
    if name not in school_data:
        school_data.update({name:0})
        return school_data
add_class(school_data,'1v')
print(school_data)

def remove_class(school_data,name):
    if name in school_data:
        school_data.pop(name)
        return school_data
remove_class(school_data,'1b')
print(school_data)

def calc_students(school_data):
    return print(sum(school_data.values()))
calc_students(school_data)

"""
Написать функцию count_char, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}

Нельзя пользоваться collections.Counter!
"""
str_val = 'python is the fastest-growing major programming language'
def count_char():
    count={}
    for s in str_val:
        if s in count:
            count[s]+=1
        else:
            count[s]=1
    return count
print(count_char())

"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и
False, если нет

Нельзя пользоваться операцией возведения в степень
"""


def check_number(a):
    while a != 1 and a / 2 != 1:
        a = a - (a / 2)
        if a == int(a):
            continue
        elif a != int(a):
            return False
    if a / 2 == 1 or a == 1:
        return True
"""
С помощью декораторов реализовать конвейер сборки бургера

Написать декоратор bread, который:
 - до декорируемой функции будет печатать "</------------\\>"
 - после декорируемой функции будет печатать "<\\____________/>"


Написать декоратор tomato, который:
 - до декорируемой функции будет печатать "*** помидоры ****"

Написать декоратор salad, который:
 - до декорируемой функции будет печатать "~~~~ салат ~~~~~"

Написать декоратор cheese, который:
 - до декорируемой функции будет печатать "^^^^^ сыр ^^^^^^"

Написать декоратор onion, который:
 - до декорируемой функции будет печатать "----- лук ------"

Написать функцию beef, которая:
 - печатает "### говядина ###"

Написать функцию chicken, которая:
 - печатает "|||| курица ||||"

1) Собрать с помощью декораторов гамбургер:
    - булка
    - лук
    - помидоры
    - говядина
    - булка

2) Собрать с помощью декораторов чикенбургер:
    - булка
    - сыр
    - салат
    - курица
    - булка
"""
def bread(func):
    def start_func():
        print('</------------\\>')
        if func() is not None:
            print(func())
        print('<\\____________/>')
    return start_func


def onion(func):
    def start_func():
        print('----- лук ------')
        if func() is not None:
            print(func())
    return start_func


def tomato(func):
    def start_func():
        print('*** помидоры ****')
        if func() is not None:
            print(func())
    return start_func


def salad(func):
    def start_func():
        print('~~~~ салат ~~~~~')
        if func() is not None:
            print(func())
    return start_func


def cheese(func):
    def start_func():
        print('^^^^^ сыр ^^^^^^')
        if func() is not None:
            print(func())
    return start_func


@bread
@onion
@tomato
def beef():
    a = '### говядина ###'
    return a


@bread
@cheese
@salad
def chicken():
    a = '|||| курица ||||'
    return a




