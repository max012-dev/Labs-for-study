while True:
    surname = input('Фамилия: ')
    if surname:
        break
    else:
        print('Заполните поле')
while True:
    name = input('Имя: ')
    if name:
        break
    else:
        print('Заполните поле')
while True:
    group = input('Группа: ')
    if group:
        break
    else:
        print('Заполните поле')
while True:
    town = input('Город: ')
    if town:
        break
    else:
        print('Заполните поле')
while True:
    age = int(input('Возраст: '))
    if age in range(1, 121):
        break
    if age not in range(0, 121):
        print("Неправильно указан возраст!")
    else:
        print('Заполните поле')
while True:
    fav = input('Любимый предмет: ')
    if fav:
        break
    else:
        print('Заполните поле')
while True:
    chas = float(input('Часы подготовки в неделю: '))
    if chas <= 0:
        print("Неверный ввод!")
    else:
        break
future_age = age + 4
total_hours_4_weeks = round(chas * 4, 2)
avg_daily_hours = round(chas / 7, 2)

print("\n" + "="*40)
print(f"{'ПРОФИЛЬ СТУДЕНТА':^40}")
print("="*40)
print('ФИ:', surname, name)
print(f"Группа: {group}")
print(f"Город: {town}")
print(f"Возраст через 4 года: {future_age}")
print(f"Любимый предмет: {fav}")
print("-"*40)
print(f"Время подгот. за 4 недели: {total_hours_4_weeks:.2f} ч.")
print(f"Среднее время в день: {avg_daily_hours:.2f} ч.")
print("="*40)


