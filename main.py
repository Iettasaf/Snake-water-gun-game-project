import random
computer = random.choice([-1,0,1])
gamer = input("Enter your choice: ")
dic = {"s" : 1,"w" : -1, "g" : 0}
reverseDic = {1 : "s",-1 : "w",0 : "g"}
you = dic[gamer]
print(f"You chose {reverseDic[you]}\nComputer chose {reverseDic[computer]}")
if(computer==you):
    print("it's draw")
else:
    if(computer==-1 and you==1):
        print("you win")
    elif(computer==1 and you==-1):
        print("you lose")
    elif(computer==1 and you==0):
        print("you win")
    elif(computer==0 and you==1):
        print("you lose")
    elif(computer==0 and you==-1):
        print("you lose")
    elif(computer==-1 and you==0):
        print("you win")
    else:

        print("something went wrong")
