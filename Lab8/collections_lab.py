PUNCTUATION_TO_STRIP = ".,!?;:"

VARIANT_14_RECORDS = [
    {"title": "Открытие сезона", "category": "основное", "amount": 120},
    {"title": "Мастер-класс по Python", "category": "дополнительное", "amount": 35},
    {"title": "Хакатон факультета", "category": "основное", "amount": 80},
    {"title": "Экскурсия в технопарк", "category": "вывозное", "amount": 45},
    {"title": "Клуб настольных игр", "category": "дополнительное", "amount": 25},
    {"title": "Итоговая конференция", "category": "основное", "amount": 150},
]


def word_counts(text: str) -> dict[str, int]:
    """Возвращает словарь «слово -> количество» для текста в нижнем регистре."""
    counts: dict[str, int] = {}
    for token in text.lower().split():
        cleaned = token.strip(PUNCTUATION_TO_STRIP)
        if cleaned:
            counts[cleaned] = counts.get(cleaned, 0) + 1
    return counts


def print_word_counts(counts: dict[str, int]) -> None:
    """Выводит пары «слово: количество» по алфавиту."""
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")


def common_topics(first: list[str], second: list[str]) -> list[str]:
    """Возвращает отсортированный список общих тем двух списков."""
    return sorted(set(first) & set(second))


def all_topics(first: list[str], second: list[str]) -> list[str]:
    """Возвращает отсортированный список всех уникальных тем двух списков."""
    return sorted(set(first) | set(second))


def demo_record_and_tuple() -> tuple[str, int]:
    """Создаёт словарь записи, обновляет его и демонстрирует распаковку кортежа."""
    record: dict[str, object] = {
        "title": "Словари и множества",
        "hours": 3,
    }
    record["hours"] = 4
    record["completed"] = False

    pair: tuple[str, int] = (str(record["title"]), int(record["hours"]))
    title, hours = pair
    print(f"Тема: {title}, часов: {hours}, завершено: {record['completed']}")
    return pair


def totals_by_category(records: list[dict]) -> dict[str, int]:
    """Возвращает словарь сумм amount по категориям без изменения исходных данных."""
    totals: dict[str, int] = {}
    for item in records:
        category = item["category"]
        amount = item["amount"]
        totals[category] = totals.get(category, 0) + amount
    return totals


def titles_in_category(records: list[dict], category: str) -> list[str]:
    """Возвращает названия мероприятий для заданной категории в исходном порядке."""
    return [
        item["title"]
        for item in records
        if item.get("category") == category
    ]


def sorted_category_totals(records: list[dict]) -> list[tuple[str, int]]:
    """
    Дополнительное задание: возвращает список пар (category, total),
    отсортированных сначала по убыванию amount, затем по названию категории.
    """
    totals = totals_by_category(records)
    return sorted(
        totals.items(),
        key=lambda pair: (-pair[1], pair[0]),
    )


def print_category_summary(totals: dict[str, int]) -> None:
    """Выводит сводку по категориям в алфавитном порядке."""
    for category in sorted(totals):
        print(f"{category}: {totals[category]}")


def run_interactive_demo() -> None:
    print("=== Задание 1: Частоты слов ===")
    counts = word_counts("Python, python! SQL")
    print_word_counts(counts)

    print("\n--- Задание 2: Учебные интересы ---")
    print("Общие:", common_topics(["python", "sql", "python"], ["sql", "git"]))
    print("Все:", all_topics(["python", "sql", "python"], ["sql", "git"]))

    print("\n--- Задание 3: Запись и пара ---")
    demo_record_and_tuple()

    print("\n--- Вариант 14: План мероприятий (количество участников) ---")
    totals = totals_by_category(VARIANT_14_RECORDS)
    print("Сводка по категориям (по алфавиту):")
    print_category_summary(totals)

    print("Сортировка по убыванию участников, затем по алфавиту:")
    for category, total in sorted_category_totals(VARIANT_14_RECORDS):
        print(f"  {category}: {total}")

    query = input("\nВведите категорию для поиска: ").strip()
    found = titles_in_category(VARIANT_14_RECORDS, query)
    print(f"Найдено ({query}): {found}")


if __name__ == "__main__":
    run_interactive_demo()