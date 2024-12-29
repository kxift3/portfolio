def encrypt_message(message):
    return message.replace(" ", "")[::-1]

message = input("Enter a message to encrypt: ")
encrypted = encrypt_message(message)
print(f"Encrypted message: {encrypted}")
