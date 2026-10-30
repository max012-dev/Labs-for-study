line = input("Целые числа через пробел: ")
parts = line.split()

if not parts:
    print("Нет данных")
else:
    numbers = []
    for part in parts:
        numbers.append(int(part))

    count = len(numbers)
    total_sum = sum(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    average = total_sum / count

    print(f"Количество: {count}")
    print(f"Сумма: {total_sum}")
    print(f"Минимум: {minimum}")
    print(f"Максимум: {maximum}")
    print(f"Среднее: {average:.2f}")