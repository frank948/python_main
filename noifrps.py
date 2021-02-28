import random
import sys

outcomes = [
    ['Tie', 'You lose:(', 'You win:D'],
    ['You win:D', 'Tie', 'You lose:('],
    ['You lose:(', 'You win:D', 'Tie'],
]
rps = {
    'rock': 0,
    'paper':1,
    'scissors':2
}

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
            c = random.choice(['rock','paper','scissors'])
            p = input('Make your choice!').lower()
            print('You chose', p)
            print('Comp chose', c)
            choice = rps.get(p, 3)
            c_choice = rps.get(c)
            result = outcomes[choice][c_choice]
            print(result)
            p_rounds -= 1
            if result != 'You lose:(' and result != 'Tie':
                p_score += 1
            elif result != 'You win:D' and result != 'Tie':
                c_score += 1
        except IndexError:
            print('Invalid choice, please choose again')




        print(p_rounds, 'rounds left, score:', p_score, 'comp score', c_score, '\n')
        if rounds >= p_rounds:
            if p_score > c_score:
                print('You won the game!')
            elif c_score > p_score:
                print('You lost the game:(')
            keep_playing()

main()
