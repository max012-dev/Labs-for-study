from logic import (
    add_record,
    delete_record,
    find_records,
    set_completed,
    statistics,
    validate_records,
)


def assert_raises_value_error(fn, *args, **kwargs) -> None:
    try:
        fn(*args, **kwargs)
    except ValueError:
        pass
    else:
        assert False, "Ожидалось исключение ValueError"


def test_empty_and_stats_two_categories():
    assert statistics([]) == {
        "total_count": 0,
        "completed_count": 0,
        "uncompleted_count": 0,
        "total_amount": 0,
        "category_totals": {},
    }

    items = [
        {"id": 1, "title": "Лекция", "category": "основное", "amount": 40, "completed": True},
        {"id": 2, "title": "Квест", "category": "дополнительное", "amount": 20, "completed": False},
        {"id": 3, "title": "Семинар", "category": "основное", "amount": 30, "completed": False},
    ]
    st = statistics(items)
    assert st["total_count"] == 3
    assert st["completed_count"] == 1
    assert st["uncompleted_count"] == 2
    assert st["total_amount"] == 90
    assert list(st["category_totals"].keys()) == ["дополнительное", "основное"]
    assert st["category_totals"] == {"дополнительное": 20, "основное": 70}


def test_add_duplicate_titles_and_ids_after_delete():
    items = []
    r1 = add_record(items, "  Встреча  ", " основное ", 50)
    r2 = add_record(items, "Встреча", "дополнительное", 25)
    assert r1["id"] == 1 and r1["title"] == "Встреча" and r1["completed"] is False
    assert r2["id"] == 2 and r2["title"] == "Встреча"

    assert delete_record(items, 1) is True
    assert [x["id"] for x in items] == [2]

    r3 = add_record(items, "Финал", "основное", 100)
    assert r3["id"] == 3


def test_search_case_insensitive_and_unknown_ids():
    items = [
        {"id": 2, "title": "Python Meetup", "category": "основное", "amount": 60, "completed": False},
        {"id": 1, "title": "python workshop", "category": "дополнительное", "amount": 15, "completed": True},
    ]
    found = find_records(items, "PYTHON")
    assert [x["id"] for x in found] == [1, 2]
    assert_raises_value_error(find_records, items, "   ")

    assert set_completed(items, 999, True) is False
    assert delete_record(items, 999) is False


def test_strict_types_validation():
    assert_raises_value_error(validate_records, {})
    assert_raises_value_error(
        validate_records,
        [{"id": True, "title": "А", "category": "б", "amount": 1, "completed": False}],
    )
    assert_raises_value_error(
        validate_records,
        [{"id": 1, "title": "А", "category": "б", "amount": True, "completed": False}],
    )
    assert_raises_value_error(
        validate_records,
        [{"id": 1, "title": "А", "category": "б", "amount": 1, "completed": "false"}],
    )


if __name__ == "__main__":
    test_empty_and_stats_two_categories()
    test_add_duplicate_titles_and_ids_after_delete()
    test_search_case_insensitive_and_unknown_ids()
    test_strict_types_validation()
    print("Все тесты logic пройдены.")