def _is_strict_int(value: object) -> bool:
    """Возвращает True только для обычного int (исключая bool)."""
    return type(value) is int


def validate_records(records: object) -> list[dict]:
    """
    Проверяет весь набор записей.
    Контракт:
      - Не изменяет входные данные.
      - Корень должен быть list, каждый элемент — dict с обязательными ключами:
        id (int > 0, уникальный), title (непустая str), category (непустая str),
        amount (int >= 0, не bool), completed (строго bool).
      - Дополнительные ключи сохраняются без обработки.
      - При нарушении выбрасывает ValueError.
    """
    if type(records) is not list:
        raise ValueError("Корневой элемент данных должен быть списком")

    seen_ids: set[int] = set()
    validated: list[dict] = []

    for index, item in enumerate(records):
        if type(item) is not dict:
            raise ValueError(f"Запись [{index}] должна быть словарём")

        for key in ("id", "title", "category", "amount", "completed"):
            if key not in item:
                raise ValueError(f"Запись [{index}] не содержит обязательный ключ '{key}'")

        rec_id = item["id"]
        if not _is_strict_int(rec_id) or rec_id <= 0:
            raise ValueError(f"Запись [{index}]: 'id' должен быть положительным целым числом")
        if rec_id in seen_ids:
            raise ValueError(f"Запись [{index}]: повторяющийся 'id' = {rec_id}")
        seen_ids.add(rec_id)

        title = item["title"]
        if type(title) is not str or not title.strip():
            raise ValueError(f"Запись [{index}]: 'title' должен быть непустой строкой")

        category = item["category"]
        if type(category) is not str or not category.strip():
            raise ValueError(f"Запись [{index}]: 'category' должна быть непустой строкой")

        amount = item["amount"]
        if not _is_strict_int(amount) or amount < 0:
            raise ValueError(f"Запись [{index}]: 'amount' должен быть целым числом >= 0")

        completed = item["completed"]
        if type(completed) is not bool:
            raise ValueError(f"Запись [{index}]: 'completed' должен быть логическим значением")

        copied = item.copy()
        copied["title"] = title.strip()
        copied["category"] = category.strip()
        validated.append(copied)

    return validated


def next_record_id(records: list[dict]) -> int:
    """Возвращает max(id) + 1 для непустого списка или 1 для пустого."""
    if not records:
        return 1
    return max(item["id"] for item in records) + 1


def add_record(
    records: list[dict],
    title: str,
    category: str,
    amount: int,
) -> dict:
    """
    Добавляет новое мероприятие с начальным статусом completed=False.
    Контракт:
      - Изменяет список records на месте, добавляя новый словарь.
      - Очищает краевые пробелы в title и category; проверяет их непустоту и amount >= 0.
      - Возвращает созданную запись. При некорректных аргументах выбрасывает ValueError.
    """
    if type(title) is not str or not title.strip():
        raise ValueError("Название мероприятия не должно быть пустым")
    if type(category) is not str or not category.strip():
        raise ValueError("Категория мероприятия не должна быть пустой")
    if not _is_strict_int(amount) or amount < 0:
        raise ValueError("Количество участников должно быть целым числом >= 0")

    new_item = {
        "id": next_record_id(records),
        "title": title.strip(),
        "category": category.strip(),
        "amount": amount,
        "completed": False,
    }
    records.append(new_item)
    return new_item


def find_records(records: list[dict], query: str) -> list[dict]:
    """
    Ищет записи по непустой подстроке названия без учёта регистра.
    Контракт:
      - Не изменяет records.
      - Для пустого query (после strip) выбрасывает ValueError.
      - Возвращает список совпадающих записей в порядке возрастания ID.
    """
    if type(query) is not str or not query.strip():
        raise ValueError("Поисковый запрос не должен быть пустым")

    needle = query.strip().lower()
    matches = [item.copy() for item in records if needle in item["title"].lower()]
    matches.sort(key=lambda item: item["id"])
    return matches


def set_completed(records: list[dict], record_id: int, completed: bool) -> bool:
    """
    Устанавливает статус 'completed' для записи с указанным record_id.
    Контракт:
      - Изменяет найденную запись на месте и возвращает True.
      - Если запись с record_id не найдена, список не меняет и возвращает False.
    """
    if not _is_strict_int(record_id):
        raise ValueError("ID записи должен быть целым числом")
    if type(completed) is not bool:
        raise ValueError("Статус должен быть булевым значением")

    for item in records:
        if item["id"] == record_id:
            item["completed"] = completed
            return True
    return False


def delete_record(records: list[dict], record_id: int) -> bool:
    """
    Удаляет запись с указанным record_id без перенумерации остальных записей.
    Контракт:
      - Удаляет запись из records на месте и возвращает True.
      - Если запись с record_id не найдена, список не меняет и возвращает False.
    """
    if not _is_strict_int(record_id):
        raise ValueError("ID записи должен быть целым числом")

    for index, item in enumerate(records):
        if item["id"] == record_id:
            del records[index]
            return True
    return False


def statistics(records: list[dict]) -> dict:
    """
    Вычисляет сводную статистику по текущему списку записей.
    Контракт:
      - Не изменяет records.
      - Возвращает словарь с ключами:
        total_count, completed_count, uncompleted_count, total_amount, category_totals
        (ключи category_totals упорядочены по алфавиту после strip()).
    """
    total_count = len(records)
    completed_count = sum(1 for item in records if item["completed"])
    uncompleted_count = total_count - completed_count
    total_amount = sum(item["amount"] for item in records)

    raw_categories: dict[str, int] = {}
    for item in records:
        cat = item["category"].strip()
        raw_categories[cat] = raw_categories.get(cat, 0) + item["amount"]

    sorted_categories = {cat: raw_categories[cat] for cat in sorted(raw_categories)}

    return {
        "total_count": total_count,
        "completed_count": completed_count,
        "uncompleted_count": uncompleted_count,
        "total_amount": total_amount,
        "category_totals": sorted_categories,
    }