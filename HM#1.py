# 1. Найти сумму S введенных с клавиатуры вещественных чисел

a, b, c, d, e = map (int, input().split()) 
print (a + b + c + d + e)

#1.2

a = int (input ())
b = int (input ())
c = int (input ())
d = int (input ())
e = int (input ())
print (a + b + c + d + e)

#1.3

s = 0
a = int(input())
for i in range(a):
    i = int (input())
    s+=i
print (s)

#1.4 - исправление по твоему комменту

i = int (input())
s = i
while i != 0:
    i = int (input())
    s+=i
print (s)


# 2. Написать программу, которая будет принимать целове число (день в году)
# (Считаем, что год начинается с понедельника)
# И выводит какой это день (Рабочий/Суббота/Воскресенье)

a = int (input ())
if a % 6 == 0:
    print ('Это у нас суббота, немного почилим')
elif a % 7 == 0:
    print ('Это воскресенье, отдыхаем ;)')
else:
    print ('Рабочий день, пашем(')




# 3. Программи принимает два значения скорости
# Первое в  km/h второе m/s
# Выводит следуюее сообщение (Скорости равны/ km/h больше / m/s больше)

a, b = map (int, input().split())
c = float (b * 3.6)
if c == a:
    print ('Скорости равны')
elif c > a:
    print ('m/s больше') 
else: 
    print ('km/h больше')

# 4. Программа которая проверяет, является ли введенное число простым?

a = int (input())
b = range (2, a-1)
if a > 1:
    for i in b:
        if a % int (i) == 0:
            print ('сложное')
            break
    else:
        print ('простое')
else:
    print ('Вы ввели 1 или менее')    


