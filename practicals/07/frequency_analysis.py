from collections import Counter

def most_common_letters(message):
    message = ''.join(filter(str.isalpha, message)).lower()
    letter_counts = Counter(message)
    return letter_counts.most_common(6)

message = input("Enter the encrypted message: ")
common_letters = most_common_letters(message)
for letter, count in common_letters:
    print(f"{letter}: {count} times")
