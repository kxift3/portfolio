def decrypt_with_random_interval(encrypted_message, interval):
    decrypted = encrypted_message[::interval]
    return decrypted

encrypted_message = input("Enter the encrypted message: ")
interval = int(input("Enter the interval used for encryption: "))
decrypted_message = decrypt_with_random_interval(encrypted_message, interval)
print(f"Decrypted message: {decrypted_message}")
