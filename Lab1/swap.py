first_room = input('Первая: ')
second_room = input('Вторая: ')
temp = ''
print("Исходные значения:")
print("first_room =", first_room)
print("second_room =", second_room)

temp = first_room
first_room = second_room
second_room = temp

print("\nРезультат после обмена:")
print("first_room =", first_room)
print("second_room =", second_room)