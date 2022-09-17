#Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#Пример:
#k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import *

def make_polynomial(k):
    while k>=0:
        random_num = randint(0, 100)
        match k:
            case 1:
                print(f'{random_num}*x +', end = ' ')
            case 0:
                print(f'{random_num} =', end = ' 0')
            case _:
                print(f'{random_num}*x^{k} +', end = ' ')
        k -= 1


num = int(input('Введите степень многочлена: '))
make_polynomial(num)
        

