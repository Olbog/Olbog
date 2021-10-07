'''
1 Создайте декоратор, который обернет любую функцию и будет выполнять:
вывод строки до выполнения функции: «Код до выполнения функции»;
выполнение переданной функции;
вывод строки после выполнения функции: «Код после выполнения функции».
'''


def new_decorator(func):
    def decorated_function(*args, **kwargs):
        print('Код до выполнения функции')
        res = func(*args, **kwargs)
        print(res)
        print('Код после выполнения функции')
    return decorated_function

arg_1 = int(input())
arg_2 = int(input())

@new_decorator
def sum(a, b):
    return a + b

sum(arg_1, arg_2)


