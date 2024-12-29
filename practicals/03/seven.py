number = int(input("Enter the number for the times table (0-12 or negative for reverse): "))

if 0 <= number <= 12:
    for i in range(13):
        print(f"{i} x {number} = {i * number}")
elif -12 <= number < 0:
    for i in range(12, -1, -1):
        print(f"{i} x {abs(number)} = {i * abs(number)}")
else:
    print("Error: Please enter a number between -12 and 12.")
