# # Реализуем функцию binary_sum(), которая принимает на вход два двоичных числа в виде строк и возвращает их сумму.
# # Вычисленная сумма также должна быть бинарным числом в виде строки:

# # binary_sum('10', '1')      # 11
# # binary_sum('1101', '101')  # 10010

from math import *
binary_1=input("Введите первое двоичное число>>>>")
binary_2=input("Введите второе двоичное число>>>>>:")
def binary_sum(first, second):
    first=int(first, 2)
    second=int(second, 2)
#     переводим оба числа в десятичное представление
    sum=first+second
#     суммируем значения
    binary=bin(sum)[2:]
#     обратно переводим в двоичный вид и сразу вырезаем начальные символы "0b" которые появляются при вызове функции bin(x)
    return binary


print(binary_sum(binary_1, binary_2))


