#Дополнительное задание
line = input("Целые числа через пробел: ")
parts = line.split()
numbers = []
for part in parts:
    numbers.append(int(part))

unique_numbers = []
for number in numbers:
    if number not in unique_numbers:    #Проверка на повторы
        unique_numbers.append(number)

print(f"Без повторов: {unique_numbers}")