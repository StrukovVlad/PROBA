from itertools import count

iterator = count(start=0.0, step = 0.5)

a = list(next(iterator) for _ in range(0,20))

print(a)

