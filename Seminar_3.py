# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# #       0  1  2  3  4  5  6  7
# list = [2, 3, 5, 9, 3, 8, 5, 2]
# i = 1
# sum = 0
# print("-> на нечётных позициях элементы")
# while i <= len(list):
#     print(list[i])
#     sum = sum + list[i]
#     i += 2
# print("сумма элементов на нечетных позициях: ", sum)



# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# n = int(input("Введите количество элементов в списке: ")) 
# import random 
# list = [random.randint(1, 100) for i in range(n)]
# i = 1
# res = []
# res.append(list[0]*list[-1])
# while i < len(list)/2:
#     mult = list[i]*list[-1-i]
#     i += 1
#     res.append(mult)
# print(list, '->',  res)



# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# from random import uniform

# def get_list (n, first, last):
#     return [round(uniform(first,last), 2) for i in range(n)]

# firstlist = get_list (5, 1, 12)
# i = 0
# secondlist = []
# while i < len(firstlist):
#     num = firstlist[i]%1 
#     secondlist.append(num)
#     i += 1
# print(firstlist)
# result = max(secondlist) - min(secondlist)
# print(max(secondlist), '-', min(secondlist), '=', round(result,2))


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# n = int(input("Введите число: ")) 
# res = str()
# while n > 0:
#     res = str(n % 2) + res
#     n = n // 2
# print('В двоичной сисмеме =', res)


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

n = int(input("Введите число: "))

def fib(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n-1):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums

result = fib(n)
print(result)
