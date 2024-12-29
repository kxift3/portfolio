def is_valid_number(num):
    return 0 <= num <= 100

number = int(input("Enter a number between 0 and 100: "))
if is_valid_number(number):
    print("Valid number!")
else:
    print("Invalid number!")
