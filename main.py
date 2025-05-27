import random
from hangman_word_list import word_list
from hangman_art import stages, logo

lives = 6

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"░░░░░░░░░░░░░░░░░░░░ {lives} of 6 LIVES LEFT ░░░░░░░░░░░░░░░░░░░░")
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You've already guessed \"{guess}\".")

    display = ""
    if guess in chosen_word and guess not in correct_letters:
        correct_letters.append(guess)

    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"There's no letter \"{guess}\" in the word. You lost a life!")

        if lives == 0:
            game_over = True
            print(f'░░░░░░░░░░░░░░░░░░░░ THE WORD WAS "{chosen_word}"! YOU LOSE! ░░░░░░░░░░░░░░░░░░░░')
    if "_" not in display:
        game_over = True
        print("░░░░░░░░░░░░░░░░░░░░ YOU WIN!! ░░░░░░░░░░░░░░░░░░░░")
    print(stages[lives])
