from functions import sum_digits, average, normalize_text, select_numbers, is_palindrome

assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12

assert average([]) is None
assert average([2, 4, 6]) == 4
assert abs(average([1, 2]) - 1.5) < 1e-9

assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""

print("Базовые проверки пройдены")
print("---------------------------------------------")

#Тесты для варианта 14
test_list = [-5, 0, 2, 5]
threshold = 2
original_copy = test_list.copy()

select_numbers(test_list, threshold)
assert test_list == original_copy, "Функция не должна изменять исходный список!"
assert select_numbers([], threshold) == []
assert select_numbers([-5, 0, 2, 5], 2) == [0]
assert select_numbers([4, 1, -2, 4, 3], 1) == [4, -2, 4]
assert select_numbers([-5, 0, 2, 5], 0) == [-5, 0, 2, 5]

print("Проверки для варианта 14 пройдены")
print("---------------------------------------------")

#Тесты дополнительного задания
assert is_palindrome("шалаш") is True       # Обычное слово-палиндром в нижнем регистре
assert is_palindrome("   Топот   ") is True # Большие буквы и пробелы по бокам должны игнорироваться
assert is_palindrome("шалаш!") is False     # Восклицательный знак ломает палиндром (знаки не игнорируются)
assert is_palindrome("!-!") is True          # Чисто знаки препинания, но стоят симметрично
assert is_palindrome("Привет") is False     # Обычное слово, не палиндром
assert is_palindrome("    ") is False       # Только пробелы, после очистки строка пустая

print("Проверки для дополнительного задания пройдены")
print("---------------------------------------------")

print("Все проверки пройдены успешно!")

#assert select_numbers([-5, 0, 2, 5], 2) ==, "Этот тест упадет, так как он неправильный!"
