#Дополнительное задание
text = input("Введите текст: ")
cleaned = "".join(text.lower().split())

if not cleaned:
    print("Нет текста")
else:
    is_palindrome = True
    n = len(cleaned)
    for i in range(n // 2):
        if cleaned[i] != cleaned[n - 1 - i]:
            is_palindrome = False
            break
    if is_palindrome:
        print("Палиндром")
    else:
        print("Не палиндром")