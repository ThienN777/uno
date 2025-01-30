#2 people collaborated to make this code
#imports
import random
import time

#lists
randomnames_list=['Dragon', 'Bobert', 'Tsukareta', 'Sakura', 'Demi','Mille','Talgat','Dabuggie']
color_list = ['Blue','Yellow', 'Green', 'Red']
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
playerCards=[]
botCards=[]

#first card colors
first_cardColor = random.choice(color_list)
first_cardNumber = random.choice(number_list)
top_card = (first_cardColor, first_cardNumber)

#functions
def printtop():
    print()
    print("The top card is",*top_card)
#this function prints the current top card and the first card 

def drawCard(cardlist: list):
    color_card = random.choice(color_list)
    number_card = random.choice(number_list)
    cardlist.append((color_card,number_card))
#this function draws a card and appends it to which list enters the parameter. 

def printCardList(cardlist: list):
    for i,j in cardlist:
        print(i,j)
#this function prints the current card list 

def validCards(cardlist: list):
    global top_card
    vList=[]
    for i in cardlist:
        if i[0]==top_card[0] or i[1]==top_card[1]:
            vList.append(i)
    return vList
#checks what cards are valid to place down and puts it in vList

def amount_cards(cardlist: list):
    if len(cardlist) == 1:
        return True
#checks the amount of cards in the list

def distribute(cardlist: list):
    for i in range(amount):
        cardlist.append((random.choice(color_list),random.choice(number_list)))
#distribution of cards at the beginning of game

def playerResponse():
    while True:
        try:
            if validCards(playerCards)==[]:
                print()
                print('You have no valid cards, therefore the game will autodraw you a card.')
                print()
                time.sleep(1)
                drawCard(playerCards)
                return top_card
            print()
            print('Your cards: ')
            printCardList(playerCards)
            ip=input("Enter which card you want to play: ")
            ip=ip.split()
            if int(ip[1]) in number_list:
                ip[1]=int(ip[1])
            ip=tuple(ip)
            print()
            if ip in validCards(playerCards):
                print("Placing down...")
                time.sleep(1)
                print("Placed!")
                playerCards.remove(ip)
                print()
                print("Your cards: ")
                printCardList(playerCards)
                print()
                current_cardColor = ip[0]
                current_cardNumber = ip[1]
                return ip
            else:
                print("You do not have this card or you are not able to play it!")
                print()
                
        except IndexError:
            print()
            print("Please type the exact card value.")
            print()
#player play

def botResponse():
    while True:
        if validCards(botCards)==[]:
            print()
            print(random_name + ' has drew a card. Your turn!')
            drawCard(botCards)
            time.sleep(1)
            return top_card
        else:
            bcard=random.choice(validCards(botCards))
            print(random_name + ' has played a',*bcard)
            time.sleep(1)
            print()
            botCards.remove(bcard)
            return bcard
#bot play

#start of code
print("Welcome to mini UNO. How many cards do you want to play with?(between 2 and 7)")
while True:
    try:
        amount = int(input(""))
        if amount < 2:
            print()
            print("The number has to be between 2 and 7. This is too low.")
        elif amount > 7:
            print()
            print("The number has to be between 2 and 7. This is too high.")
        else:
            print()
            print("Ok. " + str(amount) + " cards it is!" + " Let's get started now, shall we?")
            break
    except ValueError:
        print()
        print("Please type a number 2-7.")
while True:
    try:
        print()
        ready = input("(Y)es or (N)o.")
        ready = ready.upper()
        if ready == "Y":
            print()
            print("Ok! Let's begin!")
            print()
            break
        if ready == "N":
            print()
            print('Ok, take your time.')
    except ValueError:
        print()
        print('Please type (Y) for Yes or (N) for No.')

random_name = random.choice(randomnames_list)
print('You will be playing against ' + random_name)
print()
distribute(playerCards)
distribute(botCards)
print('Your cards: ')
printCardList(playerCards)
printtop()
print()
while True:
    top_card=playerResponse()
    check = amount_cards(playerCards)
    if check == True:
        print("You have UNO!")
    time.sleep(1)
    if playerCards==[]:
        print("You won! Good job.")
        break
    top_card=botResponse()
    check = amount_cards(botCards)
    if check == True:
        print(random_name + " has UNO!")
    time.sleep(1)
    if botCards==[]:
        print(random_name + " won! Better luck next time!")
        break
    printtop()