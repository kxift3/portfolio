def count_case_letters(string):
    uppercase_count = sum(1 for char in string if char.isupper())
    lowercase_count = sum(1 for char in string if char.islower())
    return uppercase_count, lowercase_count

input_string = input("Say something: ")
uppercase, lowercase = count_case_letters(input_string)
print(f"Uppercase letters: {uppercase}, Lowercase letters: {lowercase}")
