"""One shot attempt Worlde game."""

__author__ = "730477807"

# declares the emojis
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word: str = "python"

six_letter_guess: str = str(input("What is your 6-letter guess? "))

# while loop forcing user to input a six-character word
while len(six_letter_guess) != len(secret_word):
    print(f"That was not six letters! Try again: { six_letter_guess}")
    six_letter_guess: str = str(input("What is your 6-letter guess? "))

# outputs if secret word matches user's guess
if six_letter_guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")

index_to_check: int = 0
resulting_emoji: str = ""

# loops until index value to check is no larger than the character count of the guess
# if index to check equals that of the guess, green box is displayed, otherwise continues along and loops until boolean is False
while index_to_check < len(six_letter_guess):
    if six_letter_guess[index_to_check] == secret_word[index_to_check]:
        resulting_emoji = resulting_emoji + GREEN_BOX
    elif six_letter_guess[index_to_check] in secret_word:
        resulting_emoji = resulting_emoji + YELLOW_BOX
    else:
        resulting_emoji = resulting_emoji + WHITE_BOX
    index_to_check += 1
print(resulting_emoji)