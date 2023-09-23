# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств..

import random

length1 = int(input("введите длину первого массива: "))
mas1 = [random.randint(1, 10) for _ in range(length1)]
print(mas1)
length2 = int(input("введите длину первого массива: "))
mas2 = [random.randint(1, 10) for _ in range(length2)]
print(mas2)

intersections = list(set(mas1).intersection(mas2))
intersections.sort(reverse=False)
print("Числа, которые встречаются в обоих массивах и упорядочены:")
print(intersections)