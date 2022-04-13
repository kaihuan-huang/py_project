#import moudles
import random

#  每一次步骤都可以清空
from replit import clear

from hang_man_art import stages, logo
from hangman_word import word_list

print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_world = random.choice(word_list)
world_length = len(chosen_world)

display = []
for _ in range(world_length):
    display += '_'

while not game_is_finished:
    guess = input('Guess a letter: ').lower()

    clear()

    if guess in display:
        print(f" You've already guessed {guess} .")

    for position in range(world_length):
        letter = chosen_world[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_world:
        print(f" You guessed {guess}, that's not in the world, you lose a life. ")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print('You lost!')

    if '_' not in display:
        game_is_finished = True
        print('"You win!')
    print(stages[lives])