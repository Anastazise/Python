import math
import random

print('Введите один из знаков опрации [+, -, *, /, x^n, random, !, acos] ')

# proc = input()


class Canculator:
    def __init__(self):
        pass

    def plus(self):
        print('Введите первое число')
        a = float(input())
        print('Введите второе число')
        b = float(input())
        return a + b

    def minus(self):
        print('Введите первое число')
        a = float(input())
        print('Введите второе число')
        b = float(input())
        return a - b

    def multiply(self):
        print('Введите первое число')
        a = float(input())
        print('Введите второе число')
        b = float(input())
        return a * b

    def divide(self):
        print('Введите первое число')
        a = float(input())
        print('Введите второе число')
        b = float(input())
        return a / b

    def exp(self):
        print('Введите число')
        a = float(input())
        print('Введите степень числа')
        b = float(input())
        return a ** b

    def rand(self):
        return random.randint(0, 1000)

    def factorial(self):
        print('Введите число')
        a = float(input())
        return math.factorial(a)

    def arccos(self):
        print('Введите число')
        a = float(input())
        return math.acos(a)

    def main(self):
        proc = str(input())
        if proc == '+':
            answ = Calc.plus()
            print(answ)
        elif proc == '-':
            answ = Calc.minus()
            print(answ)
        elif proc == '*':
            answ = Calc.multiply()
            print(answ)
        elif proc == '/':
            answ = Calc.divide()
            print(answ)
        elif proc == 'x^n':
            answ = Calc.exp()
            print(answ)
        elif proc == 'random':
            answ = Calc.rand()
            print(answ)
        elif proc == '!':
            answ = Calc.factorial()
            print(answ)
        elif proc == 'acos':
            answ = Calc.arccos()
            print(answ)


Calc = Canculator()
Calc.main()

