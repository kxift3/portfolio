if __name__ == "__main__":
    sweets = int(input("How many sweets are there? "))
    pupils = int(input("How many pupils are present? "))
    sweets_per_pupil = sweets // pupils
    left_over = sweets % pupils

    sweet_word = "sweets" if sweets_per_pupil != 1 else "sweet"
    pupil_word = "pupils" if pupils != 1 else "pupil"

    print(f"Each pupil gets {sweets_per_pupil} {sweet_word}, and there are {left_over} sweets left over.")
