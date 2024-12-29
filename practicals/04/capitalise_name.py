def format_name(name):
    return name.capitalize()

name = input("Enter your name: ")
formatted_name = format_name(name)
print(f"Hello, {formatted_name}!")
