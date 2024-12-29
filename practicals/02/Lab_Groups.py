if __name__ == "__main__":
    students = int(input("How many students? "))
    group_size = int(input("Required group size? "))
    full_groups = students // group_size
    left_over = students % group_size

    group_word = "groups" if full_groups != 1 else "group"
    student_word = "students" if left_over != 1 else "student"

    print(f"There will be {full_groups} {group_word} with {left_over} {student_word} left over.")
