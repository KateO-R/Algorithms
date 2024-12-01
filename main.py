# Создаем переменную для хранения максимального элемента массива
# Перебираем весь массив, чтобы работать с каждым элементом по отдельности.
# Cравниваем текущий элемент с переменной максимального значения. Сохраняем первый элемент массива в переменную, после чего сравниваем это значение с каждым элементом массива.
# Если текущий элемент больше максимального значения, заменяем максимальное значение.
# Возвращаем максимальное значение после окончания цикла.
# В конце цикла получаем максимальное значение массива.

import math
def find_max(list):
    max_number = list[0]
    for i in list:
        if i > max_number:
            max_number = i
    return max_number

def find_min(list):
    min_number = list[0]
    for i in list:
        if i < min_number:
            min_number = i
    return min_number

numbers = [96, 145, -89, -3000, 1]
print(find_max(numbers))
print(find_min(numbers))

#5! = 1 * 2 * 3 * 4 * 5 = 120
# Сравнение числа с нулем: если число равно 0, то факториал нуля будет равен 1.
# Создание переменной для хранения итогового результата.
# Использование цикла for и range для перебирания списка из чисел до нашего числа включительно, у которого мы ищем факториал.
# Домножение результирующей переменной на текущее число в цикле.
# Возврат факториала числа после цикла.

def factorial(number):
    if number == 0:
        return 1
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result
print (factorial(6))

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
print(is_prime(16))
