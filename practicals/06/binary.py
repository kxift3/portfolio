def to_binary(number):
    return bin(number)[2:]

number = int(input("Enter a positive integer: "))
if number > 0:
    print(f"Binary representation of {number}: {to_binary(number)}")
else:
    print("Please enter a positive integer.")