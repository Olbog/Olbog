a = 136 / 7
print(int(a))

b = input('Как зовут вашего друга? ')
print(b)

c = input('Ваша фамилия? ')
print(c *3)

a = 6
b = 6.787887
c = '6'
d = a * int(b) * int(c)
print(d)


b = range(15)
while len(b) > 0:
    a = sum (b[0:2])
    b = b[2:]
    print (a)



n = int(input())
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(n))


num_1, num_2 = map(int,input().split())
def Evclid(num_1, num_2):
    while num_1 != 0 and num_2 != 0:
        if num_1 >= num_2:
            num_1 %= num_2
        else:
            num_2 %= num_1
    return num_1 or num_2

print(Evclid(num_1, num_2))


token = input('Введите символ +, -, /, * ')
a, b = map(int,input('Введите числа ').split())
if token == '*':
    result = a * b
elif token == '/':
    result = a / b
elif token == '+':
    result = a + b
elif token == '-':
    result = a - b
print(result)


a = list(i for i in range(51) if i != 13 and i != 45)
print(a)


