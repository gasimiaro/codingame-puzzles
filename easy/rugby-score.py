#https://www.codingame.com/ide/puzzle/rugby-score

score = int(input())

# Iterate over the possible number of tries (5 points each)
for tries in range(score // 5 + 1):
    for transformations in range(tries + 1):  # The number of transformations cannot exceed the number of tries
        # Calculate the remaining score after tries and transformations
        remaining_score = score - (tries * 5 + transformations * 2)
        
        # If the remaining score is divisible by 3, we can complete it with penalties/drops
        if remaining_score >= 0 and remaining_score % 3 == 0:
            penalties = remaining_score // 3
            print(tries, transformations, penalties)
