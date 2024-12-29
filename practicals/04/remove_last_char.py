def remove_last_char(string):
    if len(string) > 1:
        return string[:-1]
    return string

input_string = input("Enter a word: ")
modified_string = remove_last_char(input_string)
print(f"String after removing last character: {modified_string}")
