"""Python 3 Clone of Wordle (CWordle) for C World!"""
 
import random
from enum import Enum

PREFIX = '\x1b['
INCORRECT_COLOR = PREFIX + '1;37;40m'
WRONG_SPOT_COLOR = PREFIX + '0;30;43m'
CORRECT_COLOR = PREFIX + '0;30;42m'
END_COLOR = '\x1b[0m'


class Status(Enum):
    INCORRECT = -1
    WRONG_SPOT = 0
    CORRECT = 1

def check(soln, guess: str):
    """Scores a guessed word."""
    result_dictionary = {c: Status.INCORRECT for c in guess}
    if soln == guess:
        return {c: Status.CORRECT for c in guess}, True
    else:
        for i, c in enumerate(soln):
            if c == guess[i]:
                result_dictionary[c] = Status.CORRECT
            elif c in guess:
                result_dictionary[c] = Status.WRONG_SPOT        
    return result_dictionary, False

def print_update(update):
    """Converts a result dictionary to readable string"""
    for k in update:
        if update[k] == Status.WRONG_SPOT:
            print(WRONG_SPOT_COLOR + f' {k} ' + END_COLOR, end="|")
        elif update[k] == Status.INCORRECT:
            print(INCORRECT_COLOR + f' {k} ' + END_COLOR, end="|")
        else:
            print(CORRECT_COLOR + f' {k} ' + END_COLOR, end="|")


def main():
    print("Welcome to CWorldle")
    print("Start the game!")

    words = ['CAYDIEY', 'CHASTES', 'CHRISPY', 'CAMDANE']
    letter_bank = list('abcdefghijklmnopqrstuvwxyz')
    game_word = random.choice(words)

    print(game_word)
    while True:
        guess = input('What is your guess? >')
        result_dict, is_over = check(game_word, guess)

        if is_over:
            print(f'You found the word!')
            print_update(result_dict)
            replay = input('Play again? (Y/N)>')

            if replay.lower().strip() == 'y':
                main()
            else:
                return
        else:
            print(f'Good guess!')
            print_update(result_dict)
    


if __name__ == '__main__':
    main()

