import math
import random

print('Введите один из знаков опрации [+, -, *, /, x^n, random, !, acos] ')

proc = input()

if proc == '+':
    print('Введите первое число ')
    a = int(input())
    print('Введите второе число ')
    b = int(input())
    с = a+b
    print('Ответ: ',с)
elif proc == '-':
    print('Введите первое число ')
    a = int(input())
    print('Введите второе число ')
    b = int(input())
    с = a-b
    print('Ответ: ',с)
elif proc == '*':
    print('Введите первое число ')
    a = int(input())
    print('Введите второе число ')
    b = int(input())
    с = a * b
    print('Ответ: ',с)
elif proc == '/':
    print('Введите первое число ')
    a = float(input())
    print('Введите второе число ')
    b = float(input())
    с = a/b
    print('Ответ: ',с)
elif proc == 'x^n':
    print('Введите число ')
    a = int(input())
    print('Введите степень числа ')
    b = int(input())
    с = a ** b
    print('Ответ: ',с)
elif proc == 'random':
   print(random.randint(0,1000))
elif proc == '!':
    print('Введите число ')
    a = int(input())
    с = math.factorial(a)
    print('Ответ: ', с)
elif proc == 'acos':
    print('Введите число ')
    a = float(input())
    с = math.acos(a)
    print('Ответ: ', с)