import random
import string

def encrypt_with_random_interval(message):
    interval = random.randint(2, 20)
    encrypted = []
    for char in message:
        encrypted.append(char)
        for _ in range(interval - 1):
            encrypted.append(random.choice(string.ascii_letters))
    return ''.join(encrypted), interval

message = input("Enter a message to encrypt: ")
encrypted_message, interval_used = encrypt_with_random_interval(message)
print(f"Encrypted message: {encrypted_message}")
print(f"Interval used: {interval_used}")
