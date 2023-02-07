'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь 
в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны 
N целых чисел Ai. Последняя строка содержит число X
5
1 2 3 4 5
6
-> 

'''
from random import randint
N = int(input('Введите длину массива: '))
array = [randint(1, 20) for _ in range(N)]
print (*array)
x = int(input('Введите искомое число: '))
less_x = []
more_x  = []
if (x not in array):
    for i in range (N):
        if (array[i] < x):
            less_x.append(array[i])
        else:
            more_x.append(array[i])
    if (x-max(less_x) == min(more_x)-x):
        print (f'Ближайшие числа {max(less_x)} и {min(more_x)}')
    else:
        print (f'Ближайшее число {max(less_x)}' if (x-max(less_x) < x-min(more_x)) else f'Ближайшее число {min(more_x)}')
else:
    print (f'Ближайшее число {x}')

        

        
