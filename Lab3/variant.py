#Наличие товара от плана
value = int(input("Введите число (0-100): "))

if not (0 <= value <= 100):
    print("Ошибка диапазона")
elif 0 <= value <= 19:
    print("Малый запас")
elif 20 <= value <= 64:
    print("Средний запас")
else:
    print("Большой запас")