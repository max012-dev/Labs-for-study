from pathlib import Path

from files_lab import export_matrix_csv, read_matrix, selected_sum
from table import column_sums, row_sums


def read_positive_integer(prompt: str = "Введите положительное целое число: ") -> int:
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Ошибка: введено не целое число. Повторите ввод.")
            continue

        if value <= 0:
            print("Ошибка: число должно быть больше нуля. Повторите ввод.")
            continue

        return value


def format_report(matrix: list[list[int]]) -> str:
    r_sums = row_sums(matrix)
    c_sums = column_sums(matrix)
    variant_value = selected_sum(matrix)

    row_line = " ".join(str(x) for x in r_sums)
    col_line = " ".join(str(x) for x in c_sums)

    return (
        f"Суммы строк: {row_line}\n"
        f"Суммы столбцов: {col_line}\n"
        f"Результат варианта: {variant_value}\n"
    )


def process_files(
    input_path: Path,
    report_path: Path,
    csv_path: Path | None = None,
) -> None:
    try:
        matrix = read_matrix(input_path)
        report_content = format_report(matrix)
    except FileNotFoundError:
        print(f"Ошибка: входной файл не найден: {input_path}")
        return
    except UnicodeError as exc:
        print(f"Ошибка кодировки при чтении файла '{input_path}': {exc}")
        return
    except ValueError as exc:
        print(f"Ошибка формата данных в '{input_path}': {exc}")
        return
    except OSError as exc:
        print(f"Ошибка доступа к входному файлу '{input_path}': {exc}")
        return

    try:
        with open(report_path, "w", encoding="utf-8") as file:
            file.write(report_content)
        if csv_path is not None:
            export_matrix_csv(matrix, csv_path)
    except OSError as exc:
        print(f"Ошибка записи отчёта в '{report_path}': {exc}")
        return

    print(f"Отчёт успешно сохранён в '{report_path}'.")


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    input_file = base_dir / "matrix.txt"
    report_file = base_dir / "report.txt"
    csv_file = base_dir / "matrix.csv"

    process_files(input_file, report_file, csv_file)

    print("\nПроверка read_positive_integer():")
    positive_num = read_positive_integer("Введите положительное целое число: ")
    print(f"Получено корректное число: {positive_num}")


if __name__ == "__main__":
    main()