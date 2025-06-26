import random, sys

print("Rock Paper Scissors\n")
wins = 0
losses = 0
ties = 0

while True:
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
    
    while True:
        print("Enter (r)ock, (p)aper, (s)cissors or (q)uit:")
        playerMove = input().lower()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break 
        print('Type one of r, p, s, or q.')

    # Display what the player chose
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # Computer move
    computerMove = random.choice(['r', 'p', 's'])
    if computerMove == 'r':
        print('ROCK')
    elif computerMove == 'p':
        print('PAPER')
    elif computerMove == 's':
        print('SCISSORS')

    # Determine outcome
    if playerMove == computerMove:
        print('It is a tie!')
        ties += 1
    elif (playerMove == 'r' and computerMove == 's') or \
         (playerMove == 'p' and computerMove == 'r') or \
         (playerMove == 's' and computerMove == 'p'):
        print('You win!')
        wins += 1
    else:
        print('You lose!')
        losses += 1
