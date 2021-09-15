# 1 Выведите каждый 3 элемент списка начиная с первого и заканчивая предпоследним [3.4, 56, "Some", "Hi", 7, 3.8, 44]

# a = [3.4, 56, "Some", "Hi", 7, 3.8, 44]
# print (a[::3])

# 2 Создайте картеж с одним значением "i'm tuple" без использования встроенной функции tuple() (минимум 2 способа)

# a = ("i'm tuple",)
# print (type (a))

# d = "i'm tuple",
# print (type (d))

# b = ["i'm tuple"]
# c = (b,)
# print (type(c))


# 3 Создайте множество (set), который будет содержать ключи для словаря, описывающего ученика
# Должны быть поля ("name", ("age",), ["avg mark", "smallest mark"])

a = dict.fromkeys(['name', 'age', 'avg mark', 'smallest mark'])
d = set(a)
print (d)