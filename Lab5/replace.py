text = input("Введите текст: ")

count_colons = text.count(":")
new_text = text.replace(":", "-")

print(f"Замен: {count_colons}")
print(f"Новая строка: {new_text}")