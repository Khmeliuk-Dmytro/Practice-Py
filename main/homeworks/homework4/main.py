number = 13

mask = 1 << 2
bit_enabled = (number & mask) != 0

result = number << 3

print("3-й біт увімкнений:", bit_enabled)
print("Число після зсуву на 3 біти:", result)
