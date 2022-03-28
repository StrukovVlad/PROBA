from abc import ABC, abstractmethod


class Device(ABC):
    name = 'строка'

    @abstractmethod
    def procecc_doc(self,name):
        self.name=name



class Scanner(Device):

    def procecc_doc(self,mame):
        super().procecc_doc()
        return (f'Сканирую документ: {self.name}')


class Copier(Device):

    def process_doc(self,name):
        super().procecc_doc()
        return (f'Делаю копию : {self.name}')


class MFU(Scanner, Copier):

    def process_doc(self,name):
        super().procecc_doc()
        return (f'Сканирую и отправляю факс :{self.name}')


# name=text.txt
a = Scanner()
print(a.procecc_doc())
