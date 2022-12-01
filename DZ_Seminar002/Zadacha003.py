# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать!
# Реализовать свой метод
import random
size = int(input('введите размер массива: '))
new_list = []
for i in range (size):
    n = int(input('vvedite chislo: '))
    new_list.append(n)
print(new_list)
index_spisok = random.sample(range(0, size), size)
print (index_spisok)
sffl_list=[]
for i in range( size):
    x = new_list[index_spisok[i]]
    sffl_list.append(x)
print(sffl_list)