from functions import sum_digits, average, normalize_text, select_numbers


def main():
    try:
        user_int = int(input("Введите целое число: "))
        print(f"Сумма цифр его модуля: {sum_digits(user_int)}")
    except ValueError:
        print("Ошибка: введено не целое число.")

    print("-" * 30)

    raw_numbers = input("Введите целые числа через пробел (например, -5 0 2 5): ")
    try:
        int_list = [int(x) for x in raw_numbers.split()]
    except ValueError:
        int_list = []

    avg_result = average(int_list)
    if avg_result is None:
        print("Среднее арифметическое: Нет данных")
    else:
        print(f"Среднее арифметическое: {avg_result}")

    try:
        threshold = int(input("Введите неотрицательный порог (threshold): "))
        if threshold < 0:
            print("Порог должен быть неотрицательным!")
        else:
            filtered = select_numbers(int_list, threshold)
            print(f"Результат (кратно {threshold} + 1): {filtered}")
    except ValueError:
        print("Ошибка: порог должен быть целым числом.")

    print("-" * 30)

    user_text = input("Введите произвольный текст: ")
    print(f"Нормализованный текст: '{normalize_text(user_text)}'")


if __name__ == "__main__":
    main()