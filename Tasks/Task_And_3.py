a = map(int, input('Введите Ваши числа: ').split())
a = list(a)
for i in a:
    if i % 3 == 0:
        print (i)