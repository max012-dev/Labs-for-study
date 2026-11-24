import json
from pathlib import Path
from tempfile import TemporaryDirectory

from analysis import completion_counts, leader_tasks, select_tasks, top_users, validate_todos

SAMPLE_TODOS = [
    {"id": 1, "userId": 5, "title": "Ввод", "completed": True},
    {"id": 2, "userId": 5, "title": "Циклы", "completed": False},
    {"id": 3, "userId": 10, "title": "Строки", "completed": True},
    {"id": 4, "userId": 10, "title": "Файлы", "completed": True},
    {"id": 5, "userId": 5, "title": "Списки", "completed": True},
]

def assert_invalid(bad_data: object) -> None:
    try:
        validate_todos(bad_data)
    except ValueError:
        pass
    else:
        assert False, "Ошибка не обнаружена"

def test_sample_dataset_and_leaders():
    validated = validate_todos(SAMPLE_TODOS)
    counts = completion_counts(validated)
    assert counts == {5: 2, 10: 2}

    leaders = top_users(counts)
    assert leaders == [5, 10]

    tasks = leader_tasks(validated, leaders)
    assert [t["id"] for t in tasks] == [1, 3, 4, 5]

def test_empty_and_no_completed():
    assert completion_counts([]) == {}
    assert top_users({}) == []
    assert leader_tasks([], [1]) == []

    only_incomplete = [
        {"id": 1, "userId": 2, "title": "Задача один", "completed": False},
        {"id": 2, "userId": 3, "title": "Задача два", "completed": False},
    ]
    counts = completion_counts(only_incomplete)
    assert counts == {2: 0, 3: 0}
    assert top_users(counts) == []
    assert leader_tasks(only_incomplete, [2, 3]) == []

def test_single_and_multiple_leaders():
    single_leader_data = [
        {"id": 1, "userId": 7, "title": "А", "completed": True},
        {"id": 2, "userId": 7, "title": "Б", "completed": True},
        {"id": 3, "userId": 2, "title": "В", "completed": True},
    ]
    assert top_users(completion_counts(single_leader_data)) == [7]

    tie_leader_data = [
        {"id": 1, "userId": 9, "title": "А", "completed": True},
        {"id": 2, "userId": 3, "title": "Б", "completed": True},
    ]
    assert top_users(completion_counts(tie_leader_data)) == [3, 9]

def test_variant_14_selection():
    # Пример из таблицы: user_id=5, порог=5 -> [2] ("Циклы" имеет длину 6 >= 5, completed=False)
    res_example = select_tasks(SAMPLE_TODOS, user_id=5, parameter=5)
    assert [t["id"] for t in res_example] == [2]

    # Граница равенства длины (len("Ввод") == 4, но completed=True; добавим незавершенную длины 4)
    custom = [
        {"id": 10, "userId": 5, "title": "Код4", "completed": False},
        {"id": 11, "userId": 5, "title": "Код", "completed": False},
        {"id": 12, "userId": 5, "title": "Готово", "completed": True},
    ]
    assert [t["id"] for t in select_tasks(custom, user_id=5, parameter=4)] == [10]

    # Неизвестный пользователь и отсутствие совпадений
    assert select_tasks(SAMPLE_TODOS, user_id=999, parameter=1) == []
    assert select_tasks(SAMPLE_TODOS, user_id=5, parameter=100) == []

def test_validation_errors():
    assert_invalid({"id": 1})
    assert_invalid([
        {"id": 1, "userId": 5, "title": "А", "completed": True},
        {"id": 1, "userId": 5, "title": "Б", "completed": False},
    ])
    assert_invalid([{"id": 1, "title": "А", "completed": True}])
    assert_invalid([{"id": 1, "userId": 5, "title": "А", "completed": "false"}])
    assert_invalid([{"id": True, "userId": 5, "title": "А", "completed": True}])

def test_json_roundtrip():
    with TemporaryDirectory() as tmp:
        out_path = Path(tmp) / "selected.json"
        original = select_tasks(SAMPLE_TODOS, user_id=5, parameter=5)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(original, f, ensure_ascii=False, indent=2)

        with open(out_path, "r", encoding="utf-8") as f:
            loaded = json.load(f)
        assert loaded == original

if __name__ == "__main__":
    test_sample_dataset_and_leaders()
    test_empty_and_no_completed()
    test_single_and_multiple_leaders()
    test_variant_14_selection()
    test_validation_errors()
    test_json_roundtrip()
    print("Все проверки пройдены успешно.")