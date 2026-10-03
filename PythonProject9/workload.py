name1 = input("Название 1-го предмета: ")
count1 = int(input("Количество занятий за неделю (целое неотрицательное): "))
duration1 = int(input("Продолжительность одного занятия в минутах (целое положительное): "))

name2 = input("Название 2-го предмета: ")
count2 = int(input("Количество занятий за неделю (целое неотрицательное): "))
duration2 = int(input("Продолжительность одного занятия в минутах (целое положительное): "))

sub1_minutes = count1 * duration1
sub2_minutes = count2 * duration2

total_minutes = sub1_minutes + sub2_minutes
total_hours = total_minutes / 60

available_hours = float(input(f"\nВведите ваше доступное время на неделю в часах (не меньше {total_hours:.2f}): "))

free_hours = available_hours - total_hours
four_weeks_load_minutes = total_minutes * 4

print("\n" + "="*45)
print("ИТОГИ НЕДЕЛИ".center(45))
print("="*45)

print(f"\nПредмет: {name1}")
print(f"Время: {sub1_minutes} мин.")

print(f"\nПредмет: {name2}")
print(f"Время: {sub2_minutes} мин.")

print("\n" + "-"*30)
print(f"ОБЩАЯ НАГРУЗКА:")
print(f"{total_minutes} минут")
print(f"{total_hours:.2f} часов")

print(f"\nСВОБОДНОЕ ВРЕМЯ:")
print(f"{free_hours:.2f} часов")

print(f"\nЗА 4 НЕДЕЛИ:")
print(f"{four_weeks_load_minutes} минут")
print("="*45)
