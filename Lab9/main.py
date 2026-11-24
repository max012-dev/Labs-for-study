from table import column_sums, diagonal_pattern, row_sums, transform


def read_positive_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        if raw.isdigit() and int(raw) >= 1:
            return int(raw)
        print("Введите целое число больше или равное 1.")


def read_matrix() -> list[list[int]]:
    rows = read_positive_int("Количество строк: ")
    columns = read_positive_int("Количество столбцов: ")
    matrix: list[list[int]] = []

    for row_index in range(rows):
        while True:
            parts = input(f"Строка {row_index + 1} ({columns} целых чисел): ").split()
            if len(parts) != columns:
                print(f"Нужно ровно {columns} чисел. Повторите ввод строки.")
                continue
            try:
                row = [int(part) for part in parts]
            except ValueError:
                print("Все значения в строке должны быть целыми числами.")
                continue
            matrix.append(row)
            break

    return matrix


def print_matrix(matrix: list[list[int]]) -> None:
    for row in matrix:
        print(*row)


def main() -> None:
    matrix = read_matrix()

    print("\nСуммы строк:", row_sums(matrix))
    print("Суммы столбцов:", column_sums(matrix))

    pattern_size = read_positive_int("\nВведите положительный размер узора: ")
    pattern = diagonal_pattern(pattern_size)
    print("Диагональный узор:")
    print_matrix(pattern)

    transformed = transform(matrix)
    print("\nИсходная таблица:")
    print_matrix(matrix)
    print("\nПреобразованная таблица (вариант 14):")
    print_matrix(transformed)


if __name__ == "__main__":
    main()