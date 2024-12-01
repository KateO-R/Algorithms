# Алгоритм для проверки, является ли строка палиндромом
# 1.Приведем строку к единому регистру: для отсутствия разницы между заглавными и строчными буквами, преобразуем все буквы строки в нижний регистр.
# 2.Удалим из строки все неалфавитные символы: уберём пробелы, знаки препинания и другие символы, оставив только буквы и цифры.
# 3.Сравним строку с её обратной версией: перевернём строку и сравним её с оригинальной. Если они одинаковы, значит строка — палиндром.

def is_palindrome(s):
    # Приведение строки к нижнему регистру
    s = s.lower()

    # Удаляем все неалфавитные символы
    cleaned_s = ''.join(char for char in s if char.isalnum())

    # Проверяем, равна ли строка своей обратной версии
    return cleaned_s == cleaned_s[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("2 madam"))