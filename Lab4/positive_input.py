rejected_attempts = 0

while True:
    num = int(input("Введите положительное целое число: "))
    if num > 0:
        break
    rejected_attempts += 1
square = num ** 2

print(f"Квадрат числа: {square}")
print(f"Количество отклонённых попыток: {rejected_attempts}")