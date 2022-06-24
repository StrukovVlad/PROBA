z = lambda x:x*0.5
print(z(4))

print(list(map(lambda x: x.upper(),['cat','dog','cow'])))

mag = ['1','2','5','10']
result = list(map(lambda x: int(x), mag))
print(result)

b = [5,3,0,-6,8,10,1]
result = filter(lambda x: x>0 and x%2==0, b)
print(result)
print(list(result))

from functools import reduce

print(reduce(lambda a,b: a*b, (50,57,89,12,100)))

a = [4,5,lambda: print('work'), 7,8]
print(a[2]())

num = [2,4,6,8]
lst1 = list(map(lambda x:x*2, num))
lst2 = [x*2 for x in num]
print(lst1, lst1.__sizeof__())
print(lst2, lst2.__sizeof__())


from pipe import where

lst1 = [1,2,3,5,6,8,10]
lst2 = list(lst1
            |where (lambda x:x%2==0)
            |where (lambda x: x>6))
print(lst2)