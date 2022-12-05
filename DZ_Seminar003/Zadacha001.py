# Задайте список из нескольких чисел. Напишите
# программу, которая найдёт сумму элементов списка с нечетными индексами.
#  Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
size = int(input('введите размер массива: '))
new_list = []
for i in range(size):
    new_list.append(random.randint(0,10))
print(new_list)
summa = 0
for i in range(len(new_list)):
    if i%2>0:
        summa=summa+new_list[i]
print(f'Сумма элементов массива с нечетными индексами равна {summa}')