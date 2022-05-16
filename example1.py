a=[1,2,5,7,8,9]
c=[]
for i in a:
    c.append(i**2)
print(c)


"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""
def yes_or_no(some_list):
    s = []
    for n in some_list:
        if n not in s:
            s.append(n)
            print('No')
        else:
            print('Yes')
yes_or_no([1,67,7,9,90,67])

njo
"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

"""

while True:
    """ Программка суммы цифр любого целого числа"""
    num=int(input('Введите число:'))
    s=list(str(num))
    a=[]
    count=0
    while count<=(len(s)-1):
        a.append(int(s[count]))
        count+=1
    print(sum(a))
    b=input('Желаете продолжить еще (y/n)?')
    if b=='y':
        continue
    else:
        break


"""
Написать функцию count_char, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь.
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