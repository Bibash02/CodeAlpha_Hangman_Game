# Hangman Game 

This is a simple text-based Hangman game built using Python.

The program randomly selects a word from a small predefined list of five words. The player must guess the word one letter at a time. If the guessed letter is correct, it is revealed in the word. If the guess is incorrect, the player loses one attempt.

The player is allowed a maximum of **6 incorrect guesses**. The game continues until:
- The player successfully guesses the complete word, or
- The player uses all 6 incorrect attempts.

## How It Works

- A random word is selected using the `random` module.
- A `while` loop runs the game until the player wins or loses.
- `if-else` conditions check whether the guessed letter is correct.
- A list stores all guessed letters.
- The word is displayed with underscores (`_`) for unguessed letters.

## Concepts Used

- Random module
- While loop
- If-else statements
- Lists
- Strings
- User input handling

This project is designed to demonstrate basic Python programming concepts in a simple console-based game.
