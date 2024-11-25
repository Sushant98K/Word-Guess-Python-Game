# game_logic.py

import random

hangman_art = {
    0: ("  _______  ",
        " |       |  ",
        " |          "),
    1: ("  _______  ",
        " |       |  ",
        " |       O  "),
    2: ("  _______  ",
        " |       |  ",
        " |       O  ",
        " |       |  "),
    3: ("  _______  ",
        " |       |  ",
        " |       O  ",
        " |      /|  "),
    4: ("  _______  ",
        " |       |  ",
        " |       O  ",
        " |      /|\\ "),
    5: ("  _______  ",
        " |       |  ",
        " |       O  ",
        " |      /|\\ ",
        " |      /    "),
    6: ("  _______  ",
        " |       |  ",
        " |       O  ",
        " |      /|\\ ",
        " |      / \\  "),
}

# Adding some fun descriptions for each stage
hangman_descriptions = {
    0: "Let's begin the game! No one is hanging yet!",
    1: "Oh no! The hangman is starting to appear...",
    2: "The hangman has a head! Can you save him?",
    3: "It's getting serious! The hangman has an arm!",
    4: "The hangman is fully armed! Can you guess the word?",
    5: "Oh dear! The hangman is about to take a step!",
    6: "Game over! The hangman has fully appeared!",
}

def print_hangman(stage):
    """Prints the hangman art corresponding to the current stage."""
    for line in hangman_art[stage]:
        print(line)
    print(hangman_descriptions[stage])



def display_man(wrong_guesses):
    pass

