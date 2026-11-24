import json
import socket
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

def fetch_profile(login: str) -> dict:
    cleaned = login.strip()
    if not cleaned:
        raise ValueError("Логин не должен быть пустым")

    url = "https://api.github.com/users/" + quote(cleaned, safe="")
    request = Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "python-course-lab11",
        },
    )
    with urlopen(request, timeout=10) as response:
        payload = response.read().decode("utf-8")
        data = json.loads(payload)

    if type(data) is not dict or type(data.get("login")) is not str:
        raise ValueError("Ответ не похож на профиль пользователя")
    return data


def load_sample_profile(sample_path: Path) -> dict:
    with open(sample_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    if type(data) is not dict or type(data.get("login")) is not str:
        raise ValueError("Локальный пример не содержит корректного поля 'login'")
    return data

def print_profile(profile: dict, source_label: str) -> None:
    login = profile.get("login")
    user_id = profile.get("id")
    name = profile.get("name")
    print(f"[{source_label}] login: {login} | id: {user_id} | name: {name}")


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    sample_file = base_dir / "profile_sample.json"
    output_file = base_dir / "profile.json"

    print("Выберите источник профиля:")
    print("1 — Запрос по сети (GitHub API)")
    print("2 — Локальный пример (profile_sample.json)")
    choice = input("Ваш выбор (1/2): ").strip()

    if choice == "2":
        try:
            sample_data = load_sample_profile(sample_file)
            print_profile(sample_data, "локальный пример")
        except (FileNotFoundError, UnicodeError, json.JSONDecodeError, ValueError, OSError) as exc:
            print(f"Ошибка чтения локального примера: {exc}")
        return

    login_input = input("Логин GitHub: ")
    try:
        profile_data = fetch_profile(login_input)
        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(profile_data, file, ensure_ascii=False, indent=2)
        print_profile(profile_data, "сеть")
        print(f"Сохранено в '{output_file}'.")
    except HTTPError as error:
        print(f"Сервер вернул HTTP {error.code}")
    except (URLError, TimeoutError, socket.timeout):
        print("Не удалось получить ответ по сети")
    except (ValueError, UnicodeError, json.JSONDecodeError) as error:
        print(f"Ошибка данных: {error}")
    except OSError as error:
        print(f"Ошибка доступа: {error}")

if __name__ == "__main__":
    main()