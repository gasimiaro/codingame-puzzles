#https://www.codingame.com/ide/puzzle/jack-silver-the-casino

import math

def play_roulette(rounds, initial_cash):
    cash = initial_cash

    for _ in range(rounds):
        play = input().split()
        ball = int(play[0])
        call = play[1]
        
        # Calculate bet amount (1/4 of current cash, rounded up)
        bet = math.ceil(cash / 4)
        
        # Ensure bet doesn't exceed current cash
        bet = min(bet, cash)
        
        # Process the bet
        if call == 'PLAIN':
            number = int(play[2])
            if ball == number:
                cash += bet * 35
            else:
                cash -= bet
        elif call == 'EVEN' and ball != 0 and ball % 2 == 0:
            cash += bet
        elif call == 'ODD' and ball % 2 == 1:
            cash += bet
        else:
            cash -= bet
        
        # Ensure cash doesn't go below 0
        cash = max(cash, 0)

    return cash

# Read input
rounds = int(input())
initial_cash = int(input())

# Simulate the game and print the result
final_cash = play_roulette(rounds, initial_cash)
print(final_cash)