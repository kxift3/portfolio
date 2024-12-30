def get_unique_sorted_letters(string):
    return sorted(set(string))

string = input("Enter a string: ")
unique_letters = get_unique_sorted_letters(string)
print(f"Unique letters: {unique_letters}")
