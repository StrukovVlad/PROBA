#def fib(n):
   # a,b=0,1
    #while a<n:
        #print(a,end=" ")
        #a,b=b,a+b
#fib(100)
#s='Ivanovich Aleks Izrailevich Minsk BGU 7 8 7 9 9 6 8'
#print(s.split())

proceed = 'y'
while proceed == 'y':
    num1 = float(input('Введите первое число:'))
    oper = input('Введите операцию:')
    num2 = float(input('Введите второе число:'))
    if oper == '+':
        print(num1 + num2)
    elif oper == "-":
        print(num1 - num2)
    elif oper == '*':
        print(num1 * num2)
    elif oper == '/':
        print(num1 / num2)
    else:
        print('Error')
    proceed = input("Введите 'y', чтобы продолжить или 'стоп', чтобы завершить:")
