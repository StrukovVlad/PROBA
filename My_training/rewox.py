import re

string = 'For the sake of this video ,let is pretend this log file is thousand'
string2 = 'vlad.avto@mail.ru'

downo = re.findall(r'\b[\w+]', string)
print(downo)

downo1 = re.findall(r'\w+', string)
print(downo1)

downo2 = re.findall(r'([\w+.])', string)
print(downo2)

downo3 = re.findall(r'\b(\w+ )', string)
print(downo3)