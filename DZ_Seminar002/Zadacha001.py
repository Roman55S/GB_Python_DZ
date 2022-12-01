# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
n = input('Введите десятичную дробь ')
new_list = []
for i in n:
    if i.isdigit():
        new_list.append(i)
print(new_list)
sum = 0
for i in new_list:
    sum = sum+int(i)
print(sum)
