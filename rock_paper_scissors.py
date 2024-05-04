import random
def play():
    user = input("What is your choice?'r' for Rock 'p' for paper 's' Scissors\n")
    computer = random.choice(['r' ,'p' , 's'])
    if user == computer:
        return 'tie'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You Won!'
    
    return 'You Lost'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's' ) or (player == 'p' and opponent == 'r') \
        or (player == 's' and opponent == 'p'):
        return True

print(play())