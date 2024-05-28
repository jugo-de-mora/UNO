from random import shuffle, randint

def organizar(deck):
    
    types = ['Y','B','R','G','+','C']
    finished = False
    secondList = []
    indexType = 0
    indexPrincipal = 0

    while True:
        if finished:
            break

        while True:
            continuar = True

            if len(deck) == 0:
                finished = True
                break

            if types[indexType] == deck[indexPrincipal][0]:
                secondList.append(deck.pop(indexPrincipal))
                continuar = False
        
            if continuar and indexPrincipal <= len(deck) - 1:
                indexPrincipal += 1
        
            if indexPrincipal == len(deck):
                indexPrincipal = 0
                break

        indexType += 1
    
    return secondList

def chooseColor(color):
    color_letter = ''
    if color == 'Y':
        color_letter = 'Yellow'
    elif color == 'B':
        color_letter = 'Blue'
    elif color == 'R':
        color_letter = 'Red'
    elif color == 'G':
        color_letter = 'Green'
    return color_letter

unoDeck = ['Y0','Y1','Y2','Y3','Y4','Y5','Y6','Y7','Y8','Y9',
           'B0','B1','B2','B3','B4','B5','B6','B7','B8','B9',
           'R0','R1','R2','R3','R4','R5','R6','R7','R8','R9',
           'G0','G1','G2','G3','G4','G5','G6','G7','G8','G9',
           'Y_STO','Y_STO','B_STO','R_STO','R_STO','G_STO',
           'Y+2','B+2','B+2','R+2','G+2','G+2','+4','+4',
           'C.C','C.C','C.C']
shuffle(unoDeck)

playerOne = [unoDeck.pop(0) for i in range(0,7)]        # taking the first 7 elements of the unoDeck
playerTwo = [unoDeck.pop() for i in range(-7,0)[::-1]]  # taking the last 7 elements of the unoDeck

playerOne = organizar(playerOne) # organizing both decks
playerTwo = organizar(playerTwo)

actualCard = ''
for index,card in enumerate(unoDeck):
    if card[0] != '+' and card[1].isnumeric():
        actualCard = unoDeck.pop(index)
        break

start = randint(1,2)
playerOneTurn = False
playerTwoTurn = False
if start == 1:
    playerOneTurn = True
    turn = 'one'
else:
    playerTwoTurn = True
    turn = 'two'

def deck_of(player):
    if player == 'one':
        return playerOne
    return playerTwo

counterBl = False
counter = 0
passVb = ''
cardTaken = False
playable = False
choice = ''
stop = False
myPlus = [False, ""]
colors_to_choose = {}
colors_to_choose_four = {}
color_choice = 0
color_choice_four = 0

while len(playerOne) > 0 and len(playerTwo) > 0:
    playable = False
    while not playable:
        # playerOne = organizar(playerOne) # organizing both decks
        # playerTwo = organizar(playerTwo)

        if counterBl:
            print("Counter activated:",counter)

        # if a color was setted
        if color_choice in {1,2,3}:
            color_letter = chooseColor(colors_to_choose[color_choice])
            print("Color to play:",color_letter)
        elif color_choice_four in {1,2,3,4}:
            color_letter = chooseColor(colors_to_choose_four[color_choice_four])
            print("Color to play:",color_letter)
        else:
            color_letter = chooseColor(actualCard[0])
            if actualCard == 'C.C':
                print("Current card: Color Change")
            elif actualCard[1] == '_':
                print(f"Current card: {color_letter} Stop")
            elif actualCard[0] in ('Y','B','R','G'):
                print(f"Current card: {color_letter} {actualCard[1:]}")
            else:
                print(f"Current card: {actualCard}")

        actualTurn = deck_of(turn) # deck of the actual player

        # print all the player's cards
        for x,y in enumerate(actualTurn):
            color_letter = ''
            if y[0] == 'Y':
                color_letter = 'Yellow'
            elif y[0] == 'B':
                color_letter = 'Blue'
            elif y[0] == 'R':
                color_letter = 'Red'
            elif y[0] == 'G':
                color_letter = 'Green'
            
            if y == 'C.C':
                print(f"{x}: Color Change")
            elif y[1] == '_':
                print(f"{x}: {color_letter} Stop")
            elif y[0] in ('Y','B','R','G'):
                print(f"{x}: {color_letter} {y[1:]}")
            else:
                print(f"{x}: {y}")

        # print(not cardTaken)
        # print(not counterBl)
        # print(actualCard != '+4', actualCard[1] != '+')
        # print(not myPlus[0], myPlus[1] == actualTurn)
        if not cardTaken and not counterBl and (actualCard != '+4' or actualCard[1] != '+') and (not myPlus[0] or myPlus[1] == actualTurn): # and (not myPlus[0] or myPlus[1] != actualTurn)
            print(f"{x + 1}: Take a card from the deck")  
            passVb = ''
        else:
            if counterBl and (actualCard == '+4' or actualCard[1] == '+') and (myPlus[0] and myPlus[1] != actualTurn):
                print(f"{x + 1}: Eat cards")
                passVb = 'pass'
            else:
                print(f"{x + 1}: Pass")
                passVb = 'pass'
        try:
            if turn == 'one' and stop:
                choice = int(input("Player One Turn:\n"))
                stop = False
            elif turn == 'two' and stop:
                choice = int(input("Player Two Turn:\n"))
                stop = False
            elif turn == 'one':
                choice = int(input("Player One Turn:\n"))
            else:
                choice = int(input("Player Two Turn:\n"))
        except:
            print("Just enter numbers")

        if choice in range(0,len(actualTurn)) and (not myPlus[0] or myPlus[1] != actualTurn) and (color_choice not in {1,2,3} and color_choice_four not in {1,2,3,4}):
            # if (actualTurn[choice] == '+4' or actualTurn[choice][1] == '+'):
            #     myPlus = [True, actualTurn]

            # Change color conditions
            if actualTurn[choice] == 'C.C' and (actualCard != 'C.C' or actualCard[1] != '+' or actualCard != '+4'):
                actualColor = actualCard
                actualCard = actualTurn[choice]
                playable = True
                actualTurn.pop(choice)
                cardTaken = False
                turn = 'one' if turn == 'two' else 'two'

                while color_choice not in {1,2,3}:
                    print("Choose one of the following colors:")
                    if actualColor[0] == 'Y':
                        print("1: Blue")
                        print("2: Red")
                        print("3: Green")
                        colors_to_choose = {1: 'B', 2: 'R', 3: 'G'}
                    elif actualColor[0] == 'B':
                        print("1: Yellow")
                        print("2: Red")
                        print("3: Green")
                        colors_to_choose = {1: 'Y', 2: 'R', 3: 'G'}
                    elif actualColor[0] == 'R':
                        print("1: Yellow")
                        print("2: Blue")
                        print("3: Green")
                        colors_to_choose = {1: 'Y', 2: 'B', 3: 'G'}
                    elif actualColor[0] == 'G':
                        print("1: Yellow")
                        print("2: Blue")
                        print("3: Red")
                        colors_to_choose = {1: 'Y', 2: 'B', 3: 'R'}
                    try:
                        color_choice = int(input())
                        if color_choice not in {1,2,3}:
                            print("Type a number from 1 to 3")
                    except:
                        print("Just enter numbers")
            # stop
            elif (actualCard[0] == actualTurn[choice][0] and actualTurn[choice][1] == '_') or (actualCard[1] == '_' and      actualTurn[choice][1] == '_'):
                actualCard = actualTurn[choice]
                playable = True
                stop = True
                actualTurn.pop(choice)
            # if you respond to a +2 or +4 with other plus
            elif (actualCard[1] == '+' and (actualTurn[choice][1] == '+' or
                    actualTurn[choice] == '+4')) or (actualCard[0] == actualTurn[choice][0] and 
                    (actualTurn[choice][1] == '+' or actualTurn[choice] == '+4')) or (actualTurn[choice] == '+4' and actualCard != 'C.C'):
                counterBl = True
                quantity = 2 if actualTurn[choice][1] == '+' else 4 # quantity that depends on the chosen card
                counter += quantity
                actualCard = actualTurn[choice]
                playable = True
                actualTurn.pop(choice)
                myPlus = [True, actualTurn]
                turn = 'one' if turn == 'two' else 'two'
                cardTaken = False
                print("A plus has been played")
            # any color or number
            elif (actualCard[0] == actualTurn[choice][0] or actualCard[1] == actualTurn[choice][1]) and not counterBl:
                actualCard = actualTurn[choice]
                playable = True
                actualTurn.pop(choice)
                turn = 'one' if turn == 'two' else 'two'
                cardTaken = False
            else:
                print("This card can't be played 1")
        # if a color was chosen in a mandatory way
        elif choice in range(0,len(actualTurn)) and (not myPlus[0] or myPlus[1] != actualTurn) and color_choice in {1,2,3}:
            # if the card chosen isn't a +4 or a C.C and the color chosen was the same
            if (actualTurn[choice] != '+4' and actualTurn[choice] != 'C.C') and actualTurn[choice][0] == colors_to_choose[color_choice]:
                if actualTurn[choice][1] == '+':
                    counterBl = True
                    counter += 2
                    myPlus = [True, actualTurn]
                actualCard = actualTurn[choice]
                playable = True
                actualTurn.pop(choice)
                turn = 'one' if turn == 'two' else 'two'
                cardTaken = False
                color_choice = 0 # reset this variable so as not to cause any problems
            else:
                print("This card can't be played 2.1")
        elif choice in range(0,len(actualTurn)) and (not myPlus[0] or myPlus[1] != actualTurn) and color_choice_four in {1,2,3,4}:
            # if the card chosen isn't a +4 or a C.C and the color chosen was the same
            if (actualTurn[choice] != '+4' and actualTurn[choice] != 'C.C') and actualTurn[choice][0] == colors_to_choose_four[color_choice_four]:
                if actualTurn[choice][1] == '+':
                    counterBl = True
                    counter += 2
                    myPlus = [True, actualTurn]
                actualCard = actualTurn[choice]
                playable = True
                actualTurn.pop(choice)
                turn = 'one' if turn == 'two' else 'two'
                cardTaken = False
                color_choice_four = 0
            else:
                print("This card can't be played 2.2")
        # if the actual +4 is of a specific player
        elif choice in range(0,len(actualTurn)) and myPlus[0] and myPlus[1] == actualTurn:
            # myPlus = [False, ""]
            # any stop
            if actualTurn[choice][1] == '_':
                actualCard = actualTurn[choice]
                playable = True
                stop = True
                actualTurn.pop(choice)
                myPlus = [False, ""]
            # if the respond is any plus
            elif actualTurn[choice][1] == '+' or actualTurn[choice] == '+4':
                counterBl = True
                quantity = 2 if actualTurn[choice][1] == '+' else 4 # quantity that depends on the chosen card
                counter += quantity
                actualCard = actualTurn[choice]
                playable = True
                actualTurn.pop(choice)
                turn = 'one' if turn == 'two' else 'two'
                myPlus = [True, actualTurn]
            # any color 
            elif actualTurn[choice][0] in {'Y','B','R','G'}:
                actualCard = actualTurn[choice]
                playable = True
                actualTurn.pop(choice)
                turn = 'one' if turn == 'two' else 'two'
                myPlus = [False, ""]
            else:
                print("This card can't be played 3") # this should happen if you respond with a C.C
        # if there is a counter active and no cards have been eaten yet
        elif choice == (x + 1) and passVb == 'pass' and counterBl:
            for n in range(1,counter + 1):
                actualTurn.append(unoDeck.pop(0))
            print(f"{counter} cards have been eaten")
            counterBl = False
            counter = 0
            passVb = ''
            cardTaken = False
            # myPlus = [False, ""]
            turn = 'one' if turn == 'two' else 'two'
        # if cards have been eaten, change turn (pass)
        elif choice == (x + 1) and cardTaken:
            turn = 'one' if turn == 'two' else 'two'
            cardTaken = False

            if myPlus[0] and myPlus[1] == actualTurn:
                print("Choose one of the following colors:")
                color_choice_four = 0
                print("1: Yellow")
                print("2: Blue")
                print("3: Red")
                print("4: Green")
                colors_to_choose_four = {1: 'Y', 2: 'B', 3: 'R', 4: 'G'}
                while color_choice_four not in {1,2,3,4}:
                    try:
                        color_choice_four = int(input())
                        if color_choice_four not in {1,2,3,4}:
                            print("Type a number from 1 to 4")
                    except:
                        print("Just enter numbers")

        # if take a card was chosen
        elif choice == (x + 1):
            if len(unoDeck) > 0:
                actualTurn.append(unoDeck.pop(0))
                cardTaken = True
            else:
                print("There are no more cards in the deck")
        # if the number is out of range
        else:
            print("This card doesn't exist")

if len(playerOne) == 0:
    print("Player One has won the game :D")
elif len(playerTwo) == 0:
    print("Player Two has won the game :D")
