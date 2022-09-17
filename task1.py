#Вычислить число c заданной точностью d
#Пример:
#при $d = 0.001, π = 3.141

def make_decimals(n, k):
    n = int(n * 10**k) / 10**k
    return n


num = float(input('Введите нецелое число: '))
new_num = int(input('сколько знаков после запятой оставить?: '))

print(make_decimals(num, new_num))