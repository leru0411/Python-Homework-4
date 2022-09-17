#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#"20" -> [2, 2, 5]

def Factor(n):
    new_list = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            new_list.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        new_list.append(n)
    return new_list


print(Factor(20))
        