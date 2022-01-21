"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730477807"

five_character_word: str = input("Enter a 5-character word: ")
if len(five_character_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()

matching_characters: int = 0

print("Searching for " + single_character + " in " + five_character_word)

if single_character == five_character_word[0]:
    matching_characters = matching_characters + 1
    print(single_character + " found at index 0")

if single_character == five_character_word[1]:
    matching_characters = matching_characters + 1
    print(single_character + " found at index 1")

if single_character == five_character_word[2]:
    matching_characters = matching_characters + 1
    print(single_character + " found at index 2")

if single_character == five_character_word[3]:
    matching_characters = matching_characters + 1
    print(single_character + " found at index 3")

if single_character == five_character_word[4]:
    matching_characters = matching_characters + 1
    print(single_character + " found at index 4")

if matching_characters == 1:
    print(str(matching_characters) + " instance of " + single_character + " found in " + five_character_word)
    exit()

if matching_characters > 1:
    print(str(matching_characters) + " instances of " + single_character + " found in " + five_character_word)
else:
    print("No instances of " + single_character + " found in " + five_character_word)