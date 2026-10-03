n = int(input("Введите количество чисел (n >= 1): "))

first_num = int(input("Введите число 1: "))
total_sum = first_num
positive_count = 1 if first_num > 0 else 0
maximum = first_num

for i in range(2, n + 1):
    num = int(input(f"Введите число {i}: "))
    total_sum += num
    if num > 0:
        positive_count += 1
    if num > maximum:
        maximum = num

print(f"Сумма: {total_sum}")
print(f"Количество положительных чисел: {positive_count}")
print(f"Максимум: {maximum}")