line = input("Целые числа через пробел: ")
parts = line.split()

if not parts:
    print("Нет данных")
else:
    numbers = []
    for part in parts:
        numbers.append(int(part))
    max_value = max(numbers)
    positions = []
    for index, value in enumerate(numbers):
        if value == max_value:
            positions.append(index)

print(positions)