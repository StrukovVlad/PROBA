from itertools import groupby

for key,group in groupby('Pyttthhhonnnnnist'):
    print(key, list(group))

import  itertools

result = itertools.islice('ABCDEFG',0,None,3)
for item in result:
    print(item,end = ' ')
