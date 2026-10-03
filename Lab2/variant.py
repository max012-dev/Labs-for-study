total = int(input("Введите общее количество плиток: "))
capacity = int(input("Введите вместимость одной упаковки (плиток): "))

full_units = total // capacity
remainder = total % capacity

total_units = ((total + capacity - 1) // capacity) * min(total, 1)

print(f"Полных {full_units}, остаток {remainder}, всего {total_units}")