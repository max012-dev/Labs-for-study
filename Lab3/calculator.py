num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print(f"Результат: {result:.2f}")
elif operation == "-":
    result = num1 - num2
    print(f"Результат: {result:.2f}")
elif operation == "*":
    result = num1 * num2
    print(f"Результат: {result:.2f}")
elif operation == "/":
    if num2 == 0:
        print("Деление на ноль запрещено")
    else:
        result = num1 / num2
        print(f"Результат: {result:.2f}")
else:
    print("Неизвестная операция")