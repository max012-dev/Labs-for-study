import csv
from pathlib import Path


def read_matrix(path: str | Path) -> list[list[int]]:
    file_path = Path(path)
    with open(file_path, "r", encoding="utf-8") as file:
        raw_text = file.read()

    if not raw_text:
        raise ValueError("Строка 1: файл пуст, ожидался заголовок с размерами таблицы")


    if raw_text.endswith("\n"):
        body_text = raw_text[:-1]
        if body_text.endswith("\n"):
            raise ValueError("Обнаружены лишние пустые строки в конце файла")
    else:
        body_text = raw_text

    lines = body_text.split("\n")

    for idx, line in enumerate(lines, start=1):
        if line == "" or line.strip() == "":
            raise ValueError(f"Строка {idx}: пустая или пробельная строка недопустима")

    header_parts = lines[0].split()
    if len(header_parts) != 2:
        raise ValueError("Строка 1: заголовок должен содержать два целых числа (строки и столбцы)")

    try:
        rows_count = int(header_parts[0])
        cols_count = int(header_parts[1])
    except ValueError as exc:
        raise ValueError("Строка 1: размеры таблицы должны быть целыми числами") from exc

    if rows_count <= 0 or cols_count <= 0:
        raise ValueError("Строка 1: количество строк и столбцов должно быть больше нуля")

    data_lines = lines[1:]
    expected_total_lines = 1 + rows_count
    if len(lines) != expected_total_lines:
        raise ValueError(
            f"Неверное количество строк: ожидалось {rows_count} строк данных "
            f"(всего {expected_total_lines} строк с заголовком), получено {len(data_lines)}"
        )

    matrix: list[list[int]] = []
    for offset, line in enumerate(data_lines):
        line_number = offset + 2
        tokens = line.split()
        if len(tokens) != cols_count:
            raise ValueError(
                f"Строка {line_number}: ожидалось {cols_count} чисел, получено {len(tokens)}"
            )

        row: list[int] = []
        for token in tokens:
            try:
                row.append(int(token))
            except ValueError as exc:
                raise ValueError(
                    f"Строка {line_number}: значение '{token}' не является целым числом"
                ) from exc
        matrix.append(row)

    return matrix


def selected_sum(matrix: list[list[int]]) -> int:
    """
    Вариант 14: возвращает сумму положительных элементов (значение > 0),
    находящихся в столбцах с нечётным индексом (col_idx % 2 == 1).
    Если подходящих элементов нет или матрица пуста, возвращает 0.
    """
    total = 0
    for row in matrix:
        for col_idx, value in enumerate(row):
            if col_idx % 2 == 1 and value > 0:
                total += value
    return total


def export_matrix_csv(matrix: list[list[int]], csv_path: str | Path) -> None:
    """Дополнительное задание: экспортирует таблицу в CSV через модуль csv."""
    target = Path(csv_path)
    with open(target, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        for row in matrix:
            writer.writerow(row)