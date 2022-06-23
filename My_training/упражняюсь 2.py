# import requests
#
#
#
# payload={'username': 'vladon','password':'always'}
#
# r=requests.post('https://www.bamper.by/', data=payload)
# r_dict=r.json()
# print(r_dict(['form']))

class Iterator:

    def __init__(self,start):
        self.num=start

    def __iter__(self):
        return self

    def __next__(self):
        num=self.num
        self.num+=1
        return num
n=1
#a=Counter(n)
for i in Iterator(n):
    print(i, end='')
#print(next(a))
#print(next(a))
#print(next(a))
#print(next(a))
#print(next(a))
