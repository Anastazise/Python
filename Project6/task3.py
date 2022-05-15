import math
import random

print('Введите один из знаков опрации [+, -, *, /, x^n, random, !, acos] ')

proc = input()


def plus():
    print('Введите первое число')
    a = float(input())
    print('Введите второе число')
    b = float(input())
    return a + b


def minus():
    print('Введите первое число')
    a = float(input())
    print('Введите второе число')
    b = float(input())
    return a - b


def multiply():
    print('Введите первое число')
    a = float(input())
    print('Введите второе число')
    b = float(input())
    return a * b


def divide():
    print('Введите первое число')
    a = float(input())
    print('Введите второе число')
    b = float(input())
    return a / b


def exp():
    print('Введите число')
    a = float(input())
    print('Введите степень числа')
    b = float(input())
    return a ** b


def rand():
    return random.randint(0, 1000)


def factorial():
    print('Введите число')
    a = float(input())
    return math.factorial(a)


def arccos():
    print('Введите число')
    a = float(input())
    return math.acos(a)


if proc == '+':
    answ = plus()
    print(answ)
elif proc == '-':
    answ = minus()
    print(answ)
elif proc == '*':
    answ = multiply()
    print(answ)
elif proc == '/':
    answ = divide()
    print(answ)
elif proc == 'x^n':
    answ = exp()
    print(answ)
elif proc == 'random':
    answ = rand()
    print(answ)
elif proc == '!':
    answ = factorial()
    print(answ)
elif proc == 'acos':
    answ = arccos()
    print(answ)