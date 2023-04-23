
# # Реализуйте функцию fizz_buzz, которая возвращает строку с числами (через пробел) в диапазоне от begin до end включительно.
# При этом:

# Если число делится без остатка на 3, то вместо него выводится слово Fizz
# Если число делится без остатка на 5, то вместо него выводится слово Buzz
# Если число делится без остатка и на 3, и на 5, то вместо числа выводится слово FizzBuzz
# В остальных случаях в строку добавляется само число
# Функция принимает параметры begin и end, которые определяют начало и конец диапазона включительно.
# Функция возвращает пустую строку, если диапазон пуст — в случае, когда begin > end.

# Пример
# Вызов функции:

# from solution import fizz_buzz
# print(fizz_buzz(1, 5))
# # => 1 2 Fizz 4 Buzz
# print(fizz_buzz(11, 20))
# # => 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz

begin=int(input("Введите начало диапазона>>>>>>"))
end=int(input("Введите конец диапазона>>>>>>"))
result=""
for i in range(begin, end+1):
    if begin>end:
        result=result
    elif i%3==0 and i%5==0:
        result=result + "FizzBuzz" + " "
    elif i%5==0:
        result=result + "Buzz" + " "
    elif i%3==0:
        result=result+"Fizz" + " "
    else:
        result=result+str(i) + " "
print(result)
