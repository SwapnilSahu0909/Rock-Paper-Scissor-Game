import random
computer=random.choice([1,0,-1])
your_choice=input("Enter your choice(rock/paper/scissor): ").lower()
dic={"rock":1,"paper":0,"scissor":-1}
revdic={1:"rock",0:"paper",-1:"scissor"}
you=dic[your_choice]
print(f"\nYou chose {your_choice} \nComputer chose {revdic[computer]}")

if(computer==you):
    print("DRAW")
else:
    if(computer==1 and you==0):
        print("YOU WIN")
    elif(computer==0 and you==-1):
        print("YOU WIN")
    elif(computer==-1 and you==1):
        print("YOU WIN")
    elif(computer==1 and you==-1):
        print("YOU LOSE")
    elif(computer==0 and you==1):
        print("YOU LOSE")
    elif(computer==-1 and you==0):
        print("YOU LOSE")
    else:
        print("INVALID CHOICE")
    