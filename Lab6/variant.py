line = input("Целые числа через пробел: ")
parts = line.split()

numbers = []
for part in parts:
    numbers.append(int(part))

filtered_numbers = []
for number in numbers:
    if number % 5 == 0:
        filtered_numbers.append(number)

count = len(filtered_numbers)
total_sum = sum(filtered_numbers)
sorted_copy = sorted(filtered_numbers)

print(f"Результат: {filtered_numbers}")
print(f"Количество: {count}")
print(f"Сумма: {total_sum}")
print(f"Сортированная копия: {sorted_copy}")