def letters_in_at_least_one(word1, word2):
    return sorted(set(word1) | set(word2))

def letters_in_both_words(word1, word2):
    return sorted(set(word1) & set(word2))

def letters_in_either_not_both(word1, word2):
    return sorted(set(word1) ^ set(word2))

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

print(f"Letters in at least one word: {letters_in_at_least_one(word1, word2)}")
print(f"Letters in both words: {letters_in_both_words(word1, word2)}")
print(f"Letters in either word but not both: {letters_in_either_not_both(word1, word2)}")
