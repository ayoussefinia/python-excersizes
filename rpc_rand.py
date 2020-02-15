import random 
 

print("...rock...")
print("...paper...")
print("...scissors...")
player_one = input("(enter Player 1's choice): ")

randomInnteger = random.randint(0, 2)

if randomInnteger == 0:
    player_two = "rock"
elif randomInnteger == 1:
    player_two = "paper"
else:
    player_two = "scissors"

print("SHOOT")
print(f"the computer chose {player_two}")

if player_one == "rock":
    if player_two == "scissors":
        print("player1 winds")
    elif player_two == "rock" :
        print("draw play again")
    else :
        print("player two wins")
elif player_one == "paper":
    if player_two == "scissors":
        print("player2 winds")
    elif player_two == "rock" :
        print("player1 wins")
    else :
        print("draw play again")
else :
    if player_two == "scissors":
        print("draw play again")
    elif player_two == "rock" :
        print("player2 wins")
    else :
        print("player1 wins")