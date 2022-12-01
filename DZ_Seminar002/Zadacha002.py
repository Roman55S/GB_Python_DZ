# Задайте список из n чисел последовательности (1 + 1/n)^n.
# Вывести в консоль сам список и сумму его элементов.
n = int(input('Ввелдите число '))
new_list = []
for i in range(n):
    new_list.append((1+1/(i+1))**(i+1))
print(new_list)
sum = 0
for i in new_list:
    sum = sum+i
print(sum)