import random

# predefined word list
words = ['python', 'django', 'hangman', 'java', 'css']

# randomly choose a word
secret_word = random.choice(words)

# create a list to store guessed letters
guessed_letters = []

# number of allowed incorrect guesses
incorrect_guesses = 0
max_attempts = 6

print("Welcome to the Hangman Game")
print("You have 6 incorrect guesses allowed.\n")

# game loop
while incorrect_guesses < max_attempts:
    display_word = ""

    # show guessed letters and hide others
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "-"
    
    print("Word", display_word.strip())
    print('Incorrect guesses left: ', max_attempts - incorrect_guesses)

    # check if player has guessed the word
    if "-" not in display_word:
        print("\n Congratulation you guessed the word", secret_word)
        break

    guess = input("Enter a letter: ").lower()

    # validate input
    if len(guess) != 1 or not guess.isalpha():
        print("please enter a single alhpabet letter.\n")
        continue

    if guess in guessed_letters:
        print("You already a single alphabet letter.\n")
        continue

    guessed_letters.append(guess)

    if guess not in secret_word:
        incorrect_guesses += 1
        print("Wrong guess.\n")
    else:
        print("Good guess.\n")
    
    # if player loss
    if incorrect_guesses == max_attempts:
        print("\n Game over...\n")
        print("The word was", secret_word)

