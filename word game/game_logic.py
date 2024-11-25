#game_logic.py

import random


hangman_art = {0: ("     ",
                   "     ",
                   "     "), 
               1: ("  O  ",
                   "     ",
                   "     "), 
               2: ("  O  ",
                   "  |  ",
                   "     "), 
               3: ("  O  ",
                   " /|  ",
                   "     "), 
               4: ("  O  ",
                   " /|\\ ",
                   "     "), 
               5: ("  O  ",
                   " /|\\ ",
                   " /   "), 
               6: ("  O  ",
                   " /|\\ ",
                   " / \\ ")}

for line in hangman_art[6]:
    print(line)