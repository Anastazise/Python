st = input()
i = len(st)

count = 0
c = 0

for count in st[:-1]:
    c += 1
    if c == 3:
        continue
    else:
        if count == 'c':  # английская С
            print('Найден символ С')
        else:
            print(count)