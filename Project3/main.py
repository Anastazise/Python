import math
import random

print('Введите один из знаков опрации [+, -, *, /, x^n, random, !, acos] ')

proc = input()

if proc == '+':
    a = int(input())
    b = int(input())
    с = a+b
    print(с)
elif proc == '-':
    a = int(input())
    b = int(input())
    с = a-b
    print(с)
elif proc == '*':
    a = int(input())
    b = int(input())
    с = a * b
    print(с)
elif proc == '/':
    a = float(input())
    b = float(input())
    с = a/b
    print(с)
elif proc == 'x^n':
    a = int(input())
    b = int(input())
    с = a ** b
    print(с)
elif proc == 'random':
   print(random.randint(0,1000))
elif proc == '!':
    a = int(input())
    print(math.factorial(a))
elif proc == 'acos':
    a = float(input())
    print(math.acos(a))