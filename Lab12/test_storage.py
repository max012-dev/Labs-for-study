from pathlib import Path
from tempfile import TemporaryDirectory

from logic import add_record, set_completed
from storage import load_records, save_records


def test_save_and_reload_roundtrip():
    with TemporaryDirectory() as tmp:
        target = Path(tmp) / "data.json"
        records = []
        add_record(records, "Старт", "основное", 70)
        r2 = add_record(records, "Кружок", "дополнительное", 12)
        set_completed(records, r2["id"], True)

        save_records(target, records)
        reloaded = load_records(target)
        assert reloaded == records


def test_corrupted_json_and_duplicate_id():
    with TemporaryDirectory() as tmp:
        broken = Path(tmp) / "broken.json"
        broken.write_text("{not valid json", encoding="utf-8")
        try:
            load_records(broken)
        except Exception:
            pass
        else:
            assert False, "Ожидалась ошибка при чтении битого JSON"

        dup = Path(tmp) / "dup.json"
        dup.write_text(
            '[{"id": 1, "title": "А", "category": "б", "amount": 1, "completed": false},'
            ' {"id": 1, "title": "В", "category": "б", "amount": 2, "completed": true}]',
            encoding="utf-8",
        )
        try:
            load_records(dup)
        except ValueError:
            pass
        else:
            assert False, "Ожидалась ValueError при повторяющемся id"


if __name__ == "__main__":
    test_save_and_reload_roundtrip()
    test_corrupted_json_and_duplicate_id()
    print("Все тесты storage пройдены.")