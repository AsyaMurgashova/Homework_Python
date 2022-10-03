''' 
Задайте список из нескольких чисел. Напишите программу, 
которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

'''
# исходный вариант решения

# list = [2, 3, 5, 9, 3, 8, 5, 2]
# i = 1
# sum = 0
# print("-> на нечётных позициях элементы")
# while i <= len(list):
#     print(list[i])
#     sum = sum + list[i]
#     i += 2
# print("сумма элементов на нечетных позициях: ", sum)



# пример с использованием map

# print("Введите числа через пробел")
# lst = list(map(int, input().split()))
# i = 1
# sum = 0
# print("-> на нечётных позициях элементы")
# while i <= len(lst):
#     print(lst[i])
#     sum = sum + lst[i]
#     i += 2
# print("сумма элементов на нечетных позициях: ", sum)



# добавила enumerate, filter и list comprehension

# lst = [2, 3, 5, 9, 3, 8, 5, 2]
# lst_enum = list(enumerate(lst))

# def odd(x):
#     return x[0] % 2

# lst_odd = list(filter(odd, lst_enum))
# print("сумма элементов на нечетных позициях: ", sum([x[1] for x in lst_odd]))


'''
Задайте последовательность чисел. Напишите программу, 
которая выведет список неповторяющихся элементов исходной последовательности.

'''

# исходный вариант решения (уже с list comprehension):

# first_list = [21, 3, 54, 92, 35, 80, 54, 21, 8, 19, 8]
# print("Исходный список: ", first_list)
# new_list = []
# [new_list.append(i) for i in first_list if i not in new_list]
# print("Неповторяющиеся элементы исходного списка: ", new_list)


# добавила map

# first_list = list(map(int, input("Введите числа через пробел:\n").split()))
# print("Исходный список: ", first_list)
# new_list = []
# [new_list.append(i) for i in first_list if i not in new_list]
# print("Неповторяющиеся элементы исходного списка: ", new_list)


'''
Задание 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

'''


# исходный вариант решения

# N = int(input("Введите число: ")) 
# a = []
# result = 1
# for i in range(1, N + 1):
#     result = result * i
#     a.append(result)
# print(a)


# вариант с list comprehension

N = int(input("Введите число: "))
a = []
a.append([(N * i) for i in range(N + 1)])
print(a)
