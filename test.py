import random
mywincount = 0
computerswincount = 0
def printing(result):
    print("My Choice:", mychoice)
    print("Computers Choice:", computer)
    print(result)
    print(f'I won {mywincount} times')
    print(f'Computer won {computerswincount} times')

choice = ["r","p","s"]
while mywincount<5 and computerswincount<5:
    mychoice = input()
    computer = random.choice(choice)
    # if(mychoice==computer):
    #     printing("Draw")
    #
    # elif(mychoice=="r"):
    #     if(computer=="p"):
    #         computerswincount += 1
    #         printing("Computer Wins the round")
    #
    #
    #     elif(computer=="s"):
    #         mywincount += 1
    #         printing("I win the round")
    #
    #
    # elif (mychoice=="p"):
    #     if (computer == "r"):
    #         mywincount += 1
    #         printing("I win the round")
    #
    #
    #     elif (computer == "s"):
    #         computerswincount += 1
    #         printing("Computer Wins the round")
    #
    #
    # elif (mychoice=="s"):
    #     if (computer == "r"):
    #         computerswincount += 1
    #         printing("Computer Wins the round")
    #
    #
    #     elif (computer == "p"):
    #         mywincount += 1
    #         printing("I win the round")
    mywincount+=1

    print(mywincount)


if(mywincount>computerswincount):
    print("I won the Game")
else:
    print("Computer Won the game")

