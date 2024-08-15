# 2 6
# 4 5 
# 1 2 
# n
# Output for Sample Input 1
# $50 fine. Move forwards 3 squares.

# 13 44
# Output for Sample Input 2
# Doubles. Move forwards 8 squares.
def jail():
    dice1, dice2 = 0, 0
    for i in range(3):
        dice1, dice2 = input().split(" ")
        dice1, dice2 = int(dice1), int(dice2)

        if (dice2 == dice1):
            print(f"Doubles. Move forwards {dice1 + dice2} squares.")
            return
    if input() == "n":
        print(f"$50 fine. Move forwards {dice2 + dice1} squares.")
    else:
        print(f"Use card. Move forwards {dice2 + dice1} squares.")

jail()
jail()
jail()