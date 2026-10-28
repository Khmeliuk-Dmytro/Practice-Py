n = 30
total = 0

for num in range(2, n + 1):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        total += num

print("Сума простих чисел від 2 до", n, ":", total)
