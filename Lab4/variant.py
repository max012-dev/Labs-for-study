n = int(input())

count = 0
total_sum = 0

for _ in range(n):
    num = int(input())
    # Условие: число кратно 5 (0 кратен любому ненулевому)
    if num % 5 == 0:
        count += 1
        total_sum += num

print(count, total_sum)
