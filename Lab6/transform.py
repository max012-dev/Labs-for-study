line = input("Целые числа через пробел: ")
numbers = []
for part in line.split():
    numbers.append(int(part))

transformed_numbers = []
for number in numbers:
    if number < 0:
        transformed_numbers.append(-number)
    else:
        transformed_numbers.append(number)

print(f"Исходный список: {numbers}")
print(f"Новый список: {transformed_numbers}")