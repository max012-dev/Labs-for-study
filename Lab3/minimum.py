a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

current_min = a

if b < current_min:
    current_min = b

if c < current_min:
    current_min = c

print("Минимум:", current_min)