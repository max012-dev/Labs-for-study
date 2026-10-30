text = input("Введите текст: ")
words = text.split()

valid_words = []

for raw_word in words:
    clean_word = raw_word.strip(".,!?;:")
    if not clean_word:
        continue
    word_lower = clean_word.lower()

    if len(word_lower) % 2 == 0:
        valid_words.append(word_lower)

if not valid_words:
    print("Нет совпадений")
    print(0)
else:
    for w in valid_words:
        print(w)
    print(len(valid_words))