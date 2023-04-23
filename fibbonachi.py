# Реализуйте функцию fib(), находящую положительные Числа Фибоначчи. Аргументом функции является порядковый номер числа.

# Формула:
# код для определения чисел Фибоначчи заданного порядкого номера
from math import sqrt
# импортируем модуль квадратного корня из математики

# f(n) = (phi^n - (1-phi)^n) / sqrt(5) - это формула Бине, позволяет вычислить любое число Фибоначчи по его порядковому номеру

def fib(number): 
    phi = (1 + sqrt(5)) / 2
    # определяем значение phi
    result = int((phi ** number - (1 - phi) ** number) // sqrt(5))
    # подставляем под формулу
    return result

print(fib(3))
# вуаля