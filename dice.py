import random

# function to roll dice
def roll_die():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return  roll

# input number of players
while True:
    players = input("Enter number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players")
    else:
        print("Invalid! try again")


# max score to reach
while True:
    max_score = input("Choose what number you want to play to (50-100): ")
    if max_score.isdigit():
        max_score = int(max_score)
        if 50 <= max_score <= 100:
            break
        else:
            print("Must be between 50 to 100")
    else:
        print("Invalid input! try again")

players_score = [0 for i in range(players)] # players scores list

# compare player scores and maximum score possible
while max(players_score) < max_score:

    end_game = 0
    # loop each players turn
    for player_idx in range(players):
        print("\nPlayer " +str(player_idx + 1)+ "'s turn!")
        print("Your total score is ", players_score[player_idx],"\n")
        current_score = 0

        # accumulate player score by rolling die
        while True:
            should_roll = input("Do you want to roll again (y/n): ")
            if should_roll.lower() != "y":
                break

            value = roll_die()

            # end turn for rolling "1"
            if value == 1:
                print("You rolled a 1! Turn over")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled: ", value)
            
            print("Your current score is ", current_score)
        players_score[player_idx] += current_score
        print("Your total score is: ", players_score[player_idx])

player_max_score = max(players_score)
winning_idx = players_score.index(player_max_score)
print("Player", winning_idx + 1, "wins with a score of", player_max_score)