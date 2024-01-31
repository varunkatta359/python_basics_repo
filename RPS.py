import random

def get_choices():
    player_choice=input("Enter your choice (rock, paper, scissors)=")
    options=['rock','paper','scissors']
    computer_choice=random.choice(options)
    choices = {'player':player_choice,'computer':computer_choice}
    return choices


def check_winner(player,computer):
    print(f'your choice is {player} and computer choice is {computer}')
    
    if player == computer:
        print('it\'s a tie')
    elif player == 'rock' and computer == 'paper':
        print('paper covers you! you lose')
    elif player == 'rock' and computer == 'scissors':
        print('rock smashes scissors! you win')
    elif player == 'paper' and computer == 'rock':
        print('you win ')
    elif player == 'paper' and computer == 'scissors':
        print('you lose')
    elif player == 'scissors' and computer == 'rock':
        print('you lose')
    elif player == 'scissors' and computer == 'paper':
        print('you win')


dict=get_choices()
print(dict)
result=check_winner(dict['player'],dict['computer'])
print(result)