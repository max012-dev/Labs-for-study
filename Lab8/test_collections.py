from collections_lab import (
    VARIANT_14_RECORDS,
    all_topics,
    common_topics,
    sorted_category_totals,
    titles_in_category,
    totals_by_category,
    word_counts,
)


def test_word_counts():
    assert word_counts("Python, python! SQL") == {"python": 2, "sql": 1}
    assert word_counts("!!!") == {}
    assert word_counts("") == {}


def test_topics():
    assert common_topics(["python", "sql", "python"], ["sql", "git"]) == ["sql"]
    assert all_topics(["python", "sql", "python"], ["sql", "git"]) == [
        "git",
        "python",
        "sql",
    ]
    assert common_topics([], ["sql", "git", "sql"]) == []
    assert all_topics([], ["sql", "git", "sql"]) == ["git", "sql"]


def test_base_records_without_mutation():
    records = [
        {"title": "A", "category": "основное", "amount": 4},
        {"title": "B", "category": "дополнительное", "amount": 2},
        {"title": "C", "category": "основное", "amount": 3},
    ]
    snapshot = [record.copy() for record in records]

    assert totals_by_category(records) == {"основное": 7, "дополнительное": 2}
    assert titles_in_category(records, "основное") == ["A", "C"]
    assert titles_in_category(records, "нет") == []
    assert totals_by_category([]) == {}
    assert records == snapshot


def test_variant_14_records_without_mutation():
    snapshot = [record.copy() for record in VARIANT_14_RECORDS]

    assert totals_by_category(VARIANT_14_RECORDS) == {
        "основное": 350,
        "дополнительное": 60,
        "вывозное": 45,
    }
    assert titles_in_category(VARIANT_14_RECORDS, "основное") == [
        "Открытие сезона",
        "Хакатон факультета",
        "Итоговая конференция",
    ]
    assert titles_in_category(VARIANT_14_RECORDS, "нет") == []
    assert sorted_category_totals(VARIANT_14_RECORDS) == [
        ("основное", 350),
        ("дополнительное", 60),
        ("вывозное", 45),
    ]
    assert VARIANT_14_RECORDS == snapshot


if __name__ == "__main__":
    test_word_counts()
    test_topics()
    test_base_records_without_mutation()
    test_variant_14_records_without_mutation()
    print("Все проверки пройдены успешно!")