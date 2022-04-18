# import requests
#
#
#
# payload={'username': 'vladon','password':'always'}
#
# r=requests.post('https://bamper.by/', data=payload)
# r_dict=r.json()
# print(r_dict(['form']))

class Counter:

    def __init__(self,start):
        self.num=start

    def __iter__(self):
        return self

    def __next__(self):
        num=self.num
        self.num+=1
        return num
n=5
a=Counter(n)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))