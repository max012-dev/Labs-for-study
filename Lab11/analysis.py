def validate_todos(data: object) -> list[dict]:
    """
    Проверяет структуру списка задач.
    Корень должен быть списком словарей с:
      - id: положительный int (не bool) и уникален
      - userId: положительный int (не bool)
      - title: непустая str (после strip)
      - completed: bool
    Дополнительные ключи допускаются. При ошибке выбрасывает ValueError.
    """
    if type(data) is not list:
        raise ValueError("Корневой элемент JSON должен быть списком задач")

    seen_ids: set[int] = set()
    validated: list[dict] = []

    for index, item in enumerate(data):
        if type(item) is not dict:
            raise ValueError(f"Элемент [{index}] должен быть объектом (словарем)")

        for required_key in ("id", "userId", "title", "completed"):
            if required_key not in item:
                raise ValueError(f"Элемент [{index}] не содержит обязательное поле '{required_key}'")

        task_id = item["id"]
        if type(task_id) is not int or task_id <= 0:
            raise ValueError(f"Элемент [{index}]: поле 'id' должно быть положительным целым числом")
        if task_id in seen_ids:
            raise ValueError(f"Элемент [{index}]: повторяющееся значение 'id' = {task_id}")
        seen_ids.add(task_id)

        user_id = item["userId"]
        if type(user_id) is not int or user_id <= 0:
            raise ValueError(f"Элемент [{index}]: поле 'userId' должно быть положительным целым числом")

        title = item["title"]
        if type(title) is not str or not title.strip():
            raise ValueError(f"Элемент [{index}]: поле 'title' должно быть непустой строкой")

        completed = item["completed"]
        if type(completed) is not bool:
            raise ValueError(f"Элемент [{index}]: поле 'completed' должно быть логическим значением")

        validated.append(item)

    return validated


def completion_counts(todos: list[dict]) -> dict[int, int]:
    """
    Возвращает словарь {user_id: количество_завершенных_задач}
    для всех пользователей из списка, включая тех, у кого 0 завершенных задач.
    """
    counts: dict[int, int] = {}
    for item in todos:
        user_id = item["userId"]
        counts.setdefault(user_id, 0)
        if item["completed"]:
            counts[user_id] += 1
    return counts


def top_users(counts: dict[int, int]) -> list[int]:
    """
    Возвращает отсортированный список user_id с максимальным количеством
    завершенных задач. Если словарь пуст или максимум равен 0, возвращает [].
    """
    if not counts:
        return []
    max_done = max(counts.values())
    if max_done <= 0:
        return []
    return sorted(user_id for user_id, done in counts.items() if done == max_done)


def leader_tasks(todos: list[dict], leaders: list[int]) -> list[dict]:
    """Возвращает завершенные задачи указанных лидеров в исходном порядке."""
    leader_set = set(leaders)
    return [
        item.copy()
        for item in todos
        if item["userId"] in leader_set and item["completed"]
    ]


def select_tasks(
    todos: list[dict],
    user_id: int,
    parameter: int | None = None,
) -> list[dict]:
    """
    Вариант 14: незавершенные задачи пользователя user_id,
    у которых длина title не меньше порога parameter (>= 0).
    Исходные записи не изменяются, порядок сохраняется.
    """
    if type(user_id) is not int or user_id <= 0:
        raise ValueError("user_id должен быть положительным целым числом")
    if parameter is not None and (type(parameter) is not int or parameter < 0):
        raise ValueError("parameter должен быть целым числом >= 0 или None")

    min_length = 0 if parameter is None else parameter
    return [
        item.copy()
        for item in todos
        if item["userId"] == user_id
        and not item["completed"]
        and len(item["title"]) >= min_length
    ]