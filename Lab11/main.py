import json
from pathlib import Path

from analysis import completion_counts, leader_tasks, select_tasks, top_users, validate_todos

def read_positive_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Ошибка: введите целое число.")
            continue
        if value <= 0:
            print("Ошибка: число должно быть больше нуля.")
            continue
        return value

def read_non_negative_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Ошибка: порог должен быть целым числом.")
            continue
        if value < 0:
            print("Ошибка: порог не может быть отрицательным.")
            continue
        return value

def write_json_file(path: Path, payload: object) -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(payload, file, ensure_ascii=False, indent=2)

def main() -> None:
    base_dir = Path(__file__).resolve().parent
    input_path = base_dir / "todos.json"
    leaders_path = base_dir / "leaders.json"
    selected_path = base_dir / "selected.json"

    try:
        with open(input_path, "r", encoding="utf-8") as file:
            raw_data = json.load(file)
        todos = validate_todos(raw_data)
    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {input_path}")
        return
    except UnicodeError as exc:
        print(f"Ошибка кодировки при чтении '{input_path}': {exc}")
        return
    except json.JSONDecodeError as exc:
        print(f"Некорректный JSON в '{input_path}': {exc}")
        return
    except ValueError as exc:
        print(f"Ошибка структуры данных: {exc}")
        return
    except OSError as exc:
        print(f"Ошибка доступа при чтении '{input_path}': {exc}")
        return

    counts = completion_counts(todos)
    leaders = top_users(counts)
    filtered_leaders = leader_tasks(todos, leaders)

    print("Выполнено задач по пользователям:")
    for uid in sorted(counts):
        print(f"  Пользователь {uid}: {counts[uid]}")
    print(f"Лидеры: {leaders}")
    print(f"ID задач лидеров: {[task['id'] for task in filtered_leaders]}")

    target_user = read_positive_int("\nВведите положительный user_id: ")
    min_title_len = read_non_negative_int("Введите порог длины названия (целое >= 0): ")
    selected = select_tasks(todos, target_user, min_title_len)
    print(f"Выбранные задачи (вариант 14): {[task['id'] for task in selected]}")

    try:
        write_json_file(leaders_path, filtered_leaders)
        write_json_file(selected_path, selected)
    except OSError as exc:
        print(f"Ошибка при сохранении результатов: {exc}")
        return

    print("Файлы leaders.json и selected.json успешно обновлены.")

if __name__ == "__main__":
    main()