import json
from pathlib import Path

from logic import (
    add_record,
    delete_record,
    find_records,
    set_completed,
    statistics,
)
from storage import load_records, save_records


def prompt_non_empty_str(prompt: str) -> str:
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Ошибка: значение не должно быть пустым. Повторите ввод.")


def prompt_non_negative_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Ошибка: введите целое число.")
            continue
        if value < 0:
            print("Ошибка: количество участников не может быть меньше 0.")
            continue
        return value


def prompt_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Ошибка: введите целое число.")


def prompt_yes_no(prompt: str) -> bool:
    while True:
        answer = input(prompt).strip().lower()
        if answer == "да":
            return True
        if answer == "нет":
            return False
        print("Введите 'да' или 'нет'.")


def show_records(records: list[dict]) -> None:
    if not records:
        print("Нет записей")
        return

    ordered = sorted(records, key=lambda item: item["id"])
    for item in ordered:
        status = "мероприятие проведено" if item["completed"] else "не проведено"
        print(
            f"ID {item['id']} | {item['title']} | категория: {item['category']} | "
            f"участников: {item['amount']} чел. | статус: {status}"
        )


def handle_add(records: list[dict]) -> None:
    title = prompt_non_empty_str("Название мероприятия: ")
    category = prompt_non_empty_str("Категория: ")
    amount = prompt_non_negative_int("Количество участников: ")
    created = add_record(records, title, category, amount)
    print(f"Добавлена запись с ID {created['id']}: {created['title']}")


def handle_search(records: list[dict]) -> None:
    query = prompt_non_empty_str("Подстрока названия для поиска: ")
    found = find_records(records, query)
    if not found:
        print("Ничего не найдено.")
        return
    show_records(found)


def handle_change_status(records: list[dict]) -> None:
    rec_id = prompt_int("Введите ID записи: ")
    print("Выберите новый статус:")
    print("1 — мероприятие проведено (выполнено)")
    print("2 — не проведено (не выполнено)")
    while True:
        choice = input("Ваш выбор (1/2): ").strip()
        if choice == "1":
            new_status = True
            break
        if choice == "2":
            new_status = False
            break
        print("Введите 1 или 2.")

    if set_completed(records, rec_id, new_status):
        print(f"Статус записи с ID {rec_id} обновлён.")
    else:
        print(f"Запись с ID {rec_id} не найдена. Данные не изменены.")


def handle_delete(records: list[dict]) -> None:
    rec_id = prompt_int("Введите ID записи для удаления: ")
    exists = any(item["id"] == rec_id for item in records)
    if not exists:
        print(f"Запись с ID {rec_id} не найдена. Список не изменён.")
        return

    if not prompt_yes_no(f"Подтвердите удаление записи с ID {rec_id} (да/нет): "):
        print("Удаление отменено.")
        return

    if delete_record(records, rec_id):
        print(f"Запись с ID {rec_id} удалена.")


def show_statistics(records: list[dict]) -> None:
    stats = statistics(records)
    print(f"Всего мероприятий: {stats['total_count']}")
    print(f"Проведено: {stats['completed_count']}")
    print(f"Не проведено: {stats['uncompleted_count']}")
    print(f"Всего участников: {stats['total_amount']}")
    print("Участников по категориям:")
    for category, total in stats["category_totals"].items():
        print(f"  {category}: {total}")


def try_save(path: Path, records: list[dict]) -> bool:
    try:
        save_records(path, records)
    except OSError as exc:
        print(f"Ошибка сохранения в '{path}': {exc}")
        return False
    print(f"Данные сохранены в '{path}'.")
    return True


def print_menu() -> None:
    print("\n=== План мероприятий (Вариант 14) ===")
    print("1. Показать записи")
    print("2. Добавить запись")
    print("3. Найти записи")
    print("4. Изменить статус")
    print("5. Удалить запись")
    print("6. Показать статистику")
    print("7. Сохранить данные")
    print("8. Выйти")


def main() -> None:
    data_path = Path(__file__).resolve().parent / "data.json"

    try:
        records = load_records(data_path)
    except FileNotFoundError:
        print(f"Файл '{data_path.name}' не найден. Начинаем с пустого списка.")
        records = []
    except json.JSONDecodeError as exc:
        print(f"Ошибка синтаксиса JSON в '{data_path.name}': {exc}. Файл не изменён.")
        return
    except UnicodeError as exc:
        print(f"Ошибка кодировки '{data_path.name}': {exc}. Файл не изменён.")
        return
    except ValueError as exc:
        print(f"Ошибка структуры данных в '{data_path.name}': {exc}. Файл не изменён.")
        return
    except OSError as exc:
        print(f"Ошибка чтения '{data_path.name}': {exc}. Файл не изменён.")
        return

    while True:
        print_menu()
        cmd = input("Выберите пункт меню (1-8): ").strip()

        if cmd == "1":
            show_records(records)
        elif cmd == "2":
            handle_add(records)
        elif cmd == "3":
            handle_search(records)
        elif cmd == "4":
            handle_change_status(records)
        elif cmd == "5":
            handle_delete(records)
        elif cmd == "6":
            show_statistics(records)
        elif cmd == "7":
            try_save(data_path, records)
        elif cmd == "8":
            if prompt_yes_no("Сохранить текущие данные перед выходом? (да/нет): "):
                if not try_save(data_path, records):
                    print("Сохранение не выполнено — остаёмся в меню.")
                    continue
            print("Работа завершена.")
            return
        else:
            print("Неверная команда. Введите номер от 1 до 8.")


if __name__ == "__main__":
    main()