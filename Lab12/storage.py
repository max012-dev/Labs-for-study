import json
from pathlib import Path

from logic import validate_records


def load_records(path: str | Path) -> list[dict]:
    """
    Загружает и проверяет список записей из JSON-файла в UTF-8.
    Выбрасывает:
      - FileNotFoundError — если файл отсутствует;
      - UnicodeError / json.JSONDecodeError — при проблемах кодировки или синтаксиса JSON;
      - ValueError — при нарушении структуры данных;
      - OSError — при ошибках файлового доступа.
    """
    file_path = Path(path)
    with open(file_path, "r", encoding="utf-8") as file:
        raw_data = json.load(file)
    return validate_records(raw_data)


def save_records(path: str | Path, records: list[dict]) -> None:
    """
    Проверяет записи и сохраняет их в JSON-файл в кодировке UTF-8.
    При ошибке записи выбрасывает OSError.
    """
    validated = validate_records(records)
    file_path = Path(path)
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(validated, file, ensure_ascii=False, indent=2)