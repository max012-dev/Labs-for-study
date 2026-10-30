def sum_digits(number):
    n = abs(number)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def normalize_text(text):
    return " ".join(text.split()).lower()

def select_numbers(numbers, threshold):    #Вариант 14
    divisor = threshold + 1
    return [x for x in numbers if x % divisor == 0]

def is_palindrome(text): #Дополнительное задание
    normalized = normalize_text(text)
    if not normalized:
        return False
    clean_text = normalized.replace(" ", "")
    return clean_text == clean_text[::-1]