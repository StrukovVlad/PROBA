while True:
    try:
        a = float(input('Введите первое число: '))
        s = input('Знак(+,-,*,/):')
        if s != '-' and s != '+' and s != '/' and s != '*':
            print('Водить только знаки!')
            break
        b = float(input('Введите второе число: '))
        if s == '+':
            print('Итог:', (a + b))
        elif s == '-':
            print('Итог:', (a - b))
        elif s == '/':
            print('Итог:', (a / b))
        elif s == '*':
            print('Итог:', (a * b))
    except ZeroDivisionError:
        print('Ошибка! Деление на ноль')
    except ValueError:
        print('Вводим только цифры!')
    c = input('Желаете продолжить ? (y,n) :')
    if c == 'y':
        continue
    else:
        break



