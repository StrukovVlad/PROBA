import re

 
string = 'vlad.avto@mail.ru'

s = re.findall(r'@(\w+).(\w+)', string)
print (s)

data = [1,2,3,4,-5,-6]

data_i = [i  for i in range(0,len(data)) if data[i]>0]

print(list(data_i))

