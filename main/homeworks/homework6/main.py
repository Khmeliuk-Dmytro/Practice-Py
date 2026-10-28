text = "hello"
shift = 3
result = ""

for char in text:
    new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    result += new_char

print("Зашифрований текст:", result)
