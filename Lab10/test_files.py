from pathlib import Path
from tempfile import TemporaryDirectory

from files_lab import export_matrix_csv, read_matrix, selected_sum

def assert_raises_value_error(path: Path, expected_substring: str | None = None) -> None:
    try:
        read_matrix(path)
    except ValueError as exc:
        if expected_substring is not None:
            assert expected_substring in str(exc), (
                f"Ожидалась подстрока '{expected_substring}' в сообщении '{exc}'"
            )
    else:
        assert False, "Ошибка не обнаружена"

def test_valid_matrices():
    with TemporaryDirectory() as directory:
        base = Path(directory)

        p1 = base / "m1.txt"
        p1.write_text("1 2\n7 -1\n", encoding="utf-8")
        assert read_matrix(p1) == [[7, -1]]

        p2 = base / "m2.txt"
        p2.write_text("1 1\n0\n", encoding="utf-8")
        assert read_matrix(p2) == [[0]]

        p3 = base / "m3.txt"
        p3.write_text("2 3\n1 -2 3\n4 0 -6\n", encoding="utf-8")
        matrix = read_matrix(p3)
        assert matrix == [[1, -2, 3], [4, 0, -6]]
        assert selected_sum(matrix) == 0

        p4 = base / "m4.txt"
        p4.write_text("2 2\n1 5\n-3 2\n", encoding="utf-8")
        assert selected_sum(read_matrix(p4)) == 7


def test_invalid_formats_and_errors():
    with TemporaryDirectory() as directory:
        base = Path(directory)

        empty_file = base / "empty.txt"
        empty_file.write_text("", encoding="utf-8")
        assert_raises_value_error(empty_file)

        bad_header_zero = base / "zero_header.txt"
        bad_header_zero.write_text("0 3\n", encoding="utf-8")
        assert_raises_value_error(bad_header_zero)

        line_count_mismatch = base / "line_mismatch.txt"
        line_count_mismatch.write_text("1 2\n1\n", encoding="utf-8")
        assert_raises_value_error(line_count_mismatch, "2")

        non_int_cell = base / "bad_cell.txt"
        non_int_cell.write_text("1 2\n1 x\n", encoding="utf-8")
        assert_raises_value_error(non_int_cell, "2")

        extra_data_line = base / "extra_line.txt"
        extra_data_line.write_text("1 1\n5\n6\n", encoding="utf-8")
        assert_raises_value_error(extra_data_line)

        missing_path = base / "missing.txt"
        try:
            read_matrix(missing_path)
        except FileNotFoundError:
            pass
        else:
            assert False, "Ошибка не обнаружена"

def test_csv_export():
    with TemporaryDirectory() as directory:
        csv_file = Path(directory) / "out.csv"
        export_matrix_csv([[1, -2, 3], [4, 0, -6]], csv_file)
        content = csv_file.read_text(encoding="utf-8")
        assert "1,-2,3" in content
        assert "4,0,-6" in content

if __name__ == "__main__":
    test_valid_matrices()
    test_invalid_formats_and_errors()
    test_csv_export()
    print("Все проверки пройдены успешно.")