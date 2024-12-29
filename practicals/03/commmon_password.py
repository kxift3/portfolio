BAD_PASSWORDS = ['password', 'letmein', 'opensesame', '123', 'password123']

password1 = input("Enter a new password: ")

if len(password1) < 8 or len(password1) > 12:
    print("Error: Password must be between 8 and 12 characters long.")
elif password1 in BAD_PASSWORDS:
    print("Error: This password is too common. Choose another one.")
else:
    password2 = input("Confirm your password: ")
    if password1 == password2:
        print("Password Set")
    else:
        print("Error: Passwords do not match")
