# dict = {
# 	300: 'Tito',
# 	400: 'Amiran',
# 	500: 'Denix'
# }
#
# def func(user_id):
# 	return "Hi %s !" % dict.get(user_id, 'Unknown user')
#
# print(func(300))
# print(func(600))
#

from abs import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name: str):
        self.name = name
        super().__init__()

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print(f'{self.name} says: Woof')

class Cat(Animal):
    def make_sound(self):
        print(f'{self.name} says: Meows')

Dog('Pepper').make_sound()
Cat('Bella').make_sound()














