import random
def disp():
 print(format("Welcome to the Slot Machine"," ^157"))
 print('''\n\n\n 
You'll start with £50. You'll be asked if you want to play.
Answer with yes/no. you can also use y/n
To win you must get one of the following combinations:
5\t5\t5\t\tpays\t£250
4\t4\t4 or 5 \t\tpays\t£20
3\t3\t3 or 5 \t\tpays\t£14
2\t2\t2 or 5 \t\tpays\t£10
0\t0\t0\t\tpays\t£7
0\t0\t-\t\tpays\t£5
0\t-\t-\t\tpays\t£2
7\t7\t7\t\tpays\t The Jackpot!
''')

#Constants:
INIT_STAKE = 50
INIT_BALANCE = 1000
ITEMS = ["0", "1", "2", "3", "4", "5", "7"]

firstWheel = None
secondWheel = None
thirdWheel = None
stake = INIT_STAKE
balance = INIT_BALANCE

def play():
    global stake, firstWheel, secondWheel, thirdWheel
    playQuestion = askPlayer()
    while(stake != 0 and playQuestion == True):
        firstWheel = spinWheel()
        secondWheel = spinWheel()
        thirdWheel = spinWheel()
        printScore()
        playQuestion = askPlayer()

def askPlayer():

    print("\ntype Y if you want to play, N if you dont want to and CHECK if you want to check your balance\n")

    global stake
    global balance
    while(True):
        if (balance <=1):
            print ("Machine balance reset.")
            balance = 1000

        print ("\nThe Jackpot is currently: £" + str(balance) + ".\n")
        answer = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWould you like to play? Or check your money? ")
        answer = answer.lower()
        if(answer == "yes" or answer == "y"):
            return True
        elif(answer == "no" or answer == "n"):
            print("\n\n\n\nYou ended the game with £" + str(stake) + " in your hand. Great job!\n\n\n")
          
            return False
        elif(answer == "check" or answer == "CHECK"):
            print ("\n\nYou currently have £" + str(stake) + ".")
        else:
            print("\n\n\nWhoops! Didn't get that.")

def spinWheel():
    
    randomNumber = random.randint(0, 5)
    return ITEMS[randomNumber]

def printScore():
    '''
    prints the current score
    '''
    global stake, firstWheel, secondWheel, thirdWheel, balance
    if((firstWheel == "0") and (secondWheel != "0")):
        win = 2
        balance = balance - 2
    elif((firstWheel == "0") and (secondWheel == "0") and (thirdWheel != "0")):
        win = 5
        balance = balance - 5
    elif((firstWheel == "0") and (secondWheel == "0") and (thirdWheel == "0")):
        win = 7
        balance = balance - 7
    elif((firstWheel == "2") and (secondWheel == "2") and ((thirdWheel == "2") or (thirdWheel == "5"))):
        win = 10
        balance = balance - 10
    elif((firstWheel == "3") and (secondWheel == "3") and ((thirdWheel == "3") or (thirdWheel == "5"))):
        win = 14
        balance = balance - 14
    elif((firstWheel == "4") and (secondWheel == "4") and ((thirdWheel == "4") or (thirdWheel == "5"))):
        win = 20
        balance = balance - 20
    elif((firstWheel == "5") and (secondWheel == "5") and (thirdWheel == "5")):
        win = 250
        balance = balance - 250
    elif((firstWheel == "7") and (secondWheel == "7") and (thridWheel == "7")):
        win = balance
        balance = balance - win
    else:
        win = -1
        balance = balance + 1

    stake += win
    if win == balance:
        print (format("\n\n\n\You won the JACKPOT!!"," ^157"))
    if(win > 0):
        print("\n\n",firstWheel + '\t' + secondWheel + '\t' + thirdWheel + ' -- You win £' + str(win),"\n\n\n")
        
        
    else:
        print("\n\n",firstWheel + '\t' + secondWheel + '\t' + thirdWheel + ' -- You lose\n\n\n')
        
        

