import math
import random

print('Введите один из знаков опрации [+, -, *, /, x^n, random, !, acos]')

proc = input()

if proc == '+':
    a = input()
    b = input()
    print(a + b)
else if proc == '-':
    a = input()
    b = input()
    print(a - b)
else if proc == '*':
    a = input()
    b = input()
    print(a * b)
else if proc == '/':
    a = float(input())
    b = float(input())
    print(a/b)
else if proc == 'x^n':
    a = input()
    b = input()
    print(a ** b)
else if proc == 'random':
   print(random.randint(0,1000))
else if proc == '!':
    a = input()
    print(math.factorial(a))
else if proc == 'acos':
    a = input()
    print(math.acos(a))
