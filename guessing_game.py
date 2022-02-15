import random
choices = ["r","p", "s"]
mycount = 0
computercount = 0
def printing(value):
    print("My Choice:", mychoice)
    print("Computers Choice:", computerchoice)
    print(value)
    print(f'I won {mycount} times')
    print(f'Computer won {computercount} times')

while(mycount < 5 and computercount < 5):
    mychoice = input()
    computerchoice = random.choice(choices)
    if(mychoice==computerchoice):
        printing("Draw")
    elif(mychoice=="r"):
        if(computerchoice=="p"):
            computercount += 1
            printing("Computer wins")
        elif(computerchoice=="s"):
            mycount += 1
            printing("I win")

    elif(mychoice=="p"):
        if (computerchoice == "r"):
            mycount += 1
            printing("I win")
        elif (computerchoice == "s"):
            computercount += 1
            printing("Computer wins")

    elif(mychoice=="s"):
        if (computerchoice == "r"):
            computercount += 1
            printing("Computer wins")
        elif (computerchoice == "p"):
            mycount += 1
            printing("I win")

if(mycount>computercount):
    print("I win the whole game")
else:
    print("Computer Wins the whole game")