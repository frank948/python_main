import random
import sys

outcomes = [
    ['Tie', 'You lose:(', 'You win:D'],
    ['You win:D', 'Tie', 'You lose:('],
    ['You lose:(', 'You win:D', 'Tie'],
    ['Invalid choice']
]
rps = [
    {0: 'Rock'},
    {1: 'Paper'},
    {2: 'Scissors'}
]

def main():

    def keep_playing():
        play = input('Play again? \'YES\' or \'NO\'').lower()
        if play == 'yes':
            main()
        elif play == 'no':
            'good game'
            sys.exit()
        else:
            print('Please type \'YES\' or \'NO\'')
            keep_playing()

    rounds = 0
    p_rounds = int(input('How many rounds do you want to play'))
    p_score = 0
    c_score = 0

    while p_rounds > rounds:
        try:
            c = random.choice(range(0, 3))
            p = int(input('Choose 0 for rock, 1 for paper, 2 for scissors'))
            print('You chose', rps[p][p], ',', 'computer chose', rps[c][c])
            outcome = outcomes[p][c]
            print(outcome)
            p_rounds -= 1
            if outcome != 'You lose:(' and outcome != 'Tie':
                p_score += 1
            elif outcome != 'You win:D' and outcome != 'Tie':
                c_score += 1
        except ValueError:
            print(outcomes[3][0], 'please choose an integer to represent your choice')
        except IndexError:
            print('Please choose 0, 1, or 2')

        print(p_rounds, 'rounds left, score:', p_score, 'comp score', c_score, '\n')
        if rounds >= p_rounds:
            if p_score > c_score:
                print('You won the game!')
            elif c_score > p_score:
                print('You lost the game:(')
            keep_playing()
main()
