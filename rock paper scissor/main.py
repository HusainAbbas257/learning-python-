import random
player_move=input("enter you choice(rock/paper/scissor):")
comp_move=random.choice(["rock","paper","scissor"])
print(f"computer chose:{comp_move}")
WINNER='player'
if(player_move=='rock'):
    if(comp_move=='rock'):
        winner="tie"
    elif(comp_move=='paper'):
        winner="computer"
    elif(comp_move=='scissor'):
        winner="player"
    else:
        print("something went wrong")
elif(player_move=="paper"):
    if(comp_move=='rock'):
        winner="player"
    elif(comp_move=='paper'):
        winner="tie"
    elif(comp_move=='scissor'):
        winner="computer"
    else:
        print("something went wrong")
elif(player_move=="scissor"):
    if(comp_move=='rock'):
        winner="computer"
    elif(comp_move=='paper'):
        winner="player"
    elif(comp_move=='scissor'):
        winner="tie"
    else:
        print("something went wrong")
else:
    print("something went wrong")

print(f"winner of this match is:{winner}")