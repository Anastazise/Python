import random
border = int(input()) #пограничное число
number = random.randint(0,100) #произвольное число

print(number)

if number > (border*3):
    print('Случайное число больше указанного более чем в 3 раза')
elif number < border:
    print('Случайное число меньше указанного')
elif number > border:
    print('Случайное число больше указанного')
