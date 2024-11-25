import random
from word_library import words, letters
from game_logic import print_hangman

def get_random_word(level):
    """Select a random word from the specified level."""
    return random.choice(words[level])

def print_title():
    """Prints the title of the game."""
    print("=" * 40)
    print(" " * 10 + "WELCOME TO THE WORD GUESSING GAME!")
    print("=" * 40)
    print("Type 'quit' or 'exit' at any time to leave the game.")
    print("=" * 40)

def play_game():
    level = 0
    correct_guesses = 0
    wrong_guesses = 0
    max_wrong_guesses = 6
    used_guesses = []  # List to track used guesses

    print_title()

    while level < len(words):
        current_word = get_random_word(level)
        print(f"\nLevel {level + 1}: This level contains the word '{current_word}'.")
        print("Guess three valid words using the letters: ", ' '.join(letters[level]))

        while correct_guesses < 3 and wrong_guesses < max_wrong_guesses:
            user_guess = input("Enter your guess: ").strip().lower()

            # Check if the user wants to quit
            if user_guess in ["quit", "exit"]:
                print("Thanks for playing! Goodbye!")
                return  # Exit the game

            # Check if the guess is already used
            if user_guess in used_guesses:
                print("You've already guessed that word! That's a wrong guess.")
                wrong_guesses += 1
                print(f"You have {max_wrong_guesses - wrong_guesses} guesses left.")
                print_hangman(wrong_guesses)
                continue  # Skip the rest of the loop and prompt for another guess

            # Add the guess to the used guesses list
            used_guesses.append(user_guess)

            if user_guess in words[level]:
                correct_guesses += 1
                print(f"Correct! You've guessed {correct_guesses} words.")
            else:
                wrong_guesses += 1
                print(f"Wrong guess! You have {max_wrong_guesses - wrong_guesses} guesses left.")
                print_hangman(wrong_guesses)

            if correct_guesses == 3:
                print("Congratulations! You've advanced to the next level.")
                level += 1
                correct_guesses = 0  # Reset correct guesses for the next level
                wrong_guesses = 0  # Reset wrong guesses for the next level
                used_guesses = []  # Reset used guesses for the next level
                break

        if wrong_guesses >= max_wrong_guesses:
            print("Game over! You've made too many wrong guesses.")
            break

if __name__ == "__main__":
    play_game()