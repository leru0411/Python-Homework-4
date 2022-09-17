#Задайте последовательность чисел. Напишите программу, которая выведет список
#неповторяющихся элементов исходной последовательности.


def non_repeat_nums(my_list):
    norm_list = []
    for _ in range(7):
        my_list.append(int(input('введите целое число: ')))

    for i in my_list:
        if my_list.count(i) == 1 and i not in norm_list:
            norm_list.append(i)
    return norm_list


empty_list = []
print(non_repeat_nums(empty_list))
