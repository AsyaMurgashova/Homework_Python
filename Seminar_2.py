# Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# N = input("Введите вещественное число: ")
# summ = 0
# num = N.find(".")
# if num > 1:
#     x = N.split(".") 
#     a = int(x[0])
#     b = int(x[1])
#     while (a != 0):
#         summ = summ + (a % 10)
#         a = a // 10
#     while (b != 0):
#         summ = summ + (b % 10)
#         b = b // 10
# else:
#     for digit in N:
#         if digit.isdigit():
#             summ = summ + int(digit)
# print("Сумма цифр равна:", summ)



# Задание 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# N = int(input("Введите число: ")) 
# a = []
# result = 1
# for i in range(1, N + 1):
#     result = result * i
#     a.append(result)
# print(a)



# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.
# Пример:
# Для n = 6 -> 14.072

# n = int(input("Введите число: ")) 
# a = [round((1 + 1 / x)**x, 3) for x in range (1, n + 1)]
# print(a)
# print(sum(a))



# Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

# N = int(input("Введите число N: ")) 
# a = int(input("Введите номер первого числа: "))
# b = int(input("Введите номер второго числа: "))

# from random import randint
# numbers = [randint(-N, N) for i in range(-N, N + 1)]
# print(numbers)
# result = numbers[a-1] * numbers[b-1]
# print("Произведение элементов: ", result)


# Задание 5 Реализуйте алгоритм перемешивания списка.

# n = int(input("Введите количество элементов в списке: ")) 
# import random 
# firstlist = [random.randint(1, 100) for i in range(n+1)]
# print(firstlist)
# random.shuffle(firstlist)
# print(firstlist)


# Но вы сказали, что шаффл использовать нельзя, поэтому вот:
n = int(input("Введите количество элементов в списке: ")) 
import random 
list = [random.randint(1, 100) for i in range(n+1)]
print(list)
for i in range(len(list)-1, 0, -1):
    j = random.randint(0, i + 1)
    list[i], list[j] = list[j], list[i]
print(list)

# Задание 6 Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
# Пример
# -Для "abababb" и "aba" -> 2

