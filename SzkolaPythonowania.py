import random
import pygame,os,sys,time

from pygame import display

pygame.init()

run = True  # whole program run
game = False # 'state game" 
menu = True  # 'state menu' with randomize shuffle and instructions
gameover = False # 'state gameover' with score display

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
font = pygame.font.SysFont("arial", 24)

# GFX placeholders
card2 = pygame.image.load(os.path.join("placeholders", "2.png")).convert()
card3 = pygame.image.load(os.path.join("placeholders", "3.png")).convert()
card4 = pygame.image.load(os.path.join("placeholders", "4.png")).convert()
card5 = pygame.image.load(os.path.join("placeholders", "5.png")).convert()
card6 = pygame.image.load(os.path.join("placeholders", "6.png")).convert()
card7 = pygame.image.load(os.path.join("placeholders", "7.png")).convert()
card8 = pygame.image.load(os.path.join("placeholders", "8.png")).convert()
card9 = pygame.image.load(os.path.join("placeholders", "9.png")).convert()
card10 = pygame.image.load(os.path.join("placeholders", "10.png")).convert()
card11 = pygame.image.load(os.path.join("placeholders", "11.png")).convert()
card12 = pygame.image.load(os.path.join("placeholders", "12.png")).convert()
card13 = pygame.image.load(os.path.join("placeholders", "13.png")).convert()



baseDeck = [2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,
            6,6,6,6,6,6,7,7,7,7,7,8,8,8,8,8,9,9,9,10,10,10,11,11,12,12,13,13]  # dorobic 20 Lamignat 
shuffledDeck = []

class Stack:      # stack of cards, counting quantity and value of the latest move played
    def __init__(self, value, count, cardsDisplay, stackDisplayX, stackDisplayY):
        self.value = value
        self.count = count
        self.cardsDisplay = cardsDisplay
        self.stackDisplayX = stackDisplayX
        self.stackDisplayY = stackDisplayY
        pass

stack = Stack(0,0,0,10, 220)

class Select:       # needed to operate human player cards, selecting the cards to be played and counting how many will be played
    def __init__(self, slot,count):
        self.slot = slot
        self.count = count
        pass

select = Select(0,0)

class Hand:
    def __init__(self,cardInHandDisplayX,cardInHandDisplayY,selectedCardY):
        self.cardInHandDisplayX = cardInHandDisplayX
        self.cardInHandDisplayY = cardInHandDisplayY
        self.selectedCardY = selectedCardY
        pass

playerHand = Hand(50,450,340)

class Player:   
    def __init__(self, hand, selectedToPlay,penaltyPoints,PCturn):
        self.hand = hand
        self.selectedToPlay = selectedToPlay
        self.penaltyPoints = penaltyPoints
        self.PCturn = PCturn
        pass

p1 = Player([],[0,0,0,0,0,0],0,False)
p2 = Player([],0,0,False)

PC_NO_PLAY = 3

def clearScreen():
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 0, WIDTH, HEIGHT))
    #pygame.display.flip() 

def cleanUpOnGameover():
    global baseDeck, shuffledDeck
    baseDeck = [2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,
            6,6,6,6,6,6,7,7,7,7,7,8,8,8,8,8,9,9,9,10,10,10,11,11,12,12,13,13] 
    shuffledDeck = []
    stack.value = 0
    stack.count = 0
    p1.hand = []
    p1.selectedToPlay = [0,0,0,0,0,0]
    p1.penaltyPoints = 0
    p1.PCturn = False
    p2.hand = []
    p2.selectedToPlay = 0
    p2.penaltyPoints = 0
    p2.PCturn = False
    select.slot = 0
    select.count = 0


def displayHUDinfo():
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(10, 10, 500, 60)) 
    blitTxt = font.render("Stack value: "+str(stack.value)+"     No. of cards on stack: "+str(stack.count),True, (255,0,0))
    screen.blit(blitTxt, (10,10))
    blitTxt2 = font.render("Player penalty points: "+str(p1.penaltyPoints)+"  PC penalty points: "+str(p2.penaltyPoints),True, (255,255,255))
    screen.blit(blitTxt2, (10,40))

def displayPlayerHand():
    for i in range(6):
        # hand
        whichCard = p1.hand[i]
        
        if whichCard == 0:
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(i*100, playerHand.cardInHandDisplayY, 80, 100))
        if whichCard == 2:
            screen.blit(card2, (i*100, playerHand.cardInHandDisplayY, 80,100))
        if whichCard == 3:
            screen.blit(card3, (i*100, playerHand.cardInHandDisplayY, 80,100))
        if whichCard == 4:
            screen.blit(card4, (i*100, playerHand.cardInHandDisplayY, 80,100))
        if whichCard == 5:
            screen.blit(card5, (i*100, playerHand.cardInHandDisplayY, 80,100))
        if whichCard == 6:
            screen.blit(card6, (i*100, playerHand.cardInHandDisplayY, 80,100))
        if whichCard == 7:
            screen.blit(card7, (i*100, playerHand.cardInHandDisplayY, 80,100))
        if whichCard == 8:
            screen.blit(card8, (i*100, playerHand.cardInHandDisplayY, 80,100))
        if whichCard == 9:
            screen.blit(card9, (i*100, playerHand.cardInHandDisplayY, 80,100))
        if whichCard == 10:
            screen.blit(card10, (i*100, playerHand.cardInHandDisplayY, 80,100))
        if whichCard == 11:
            screen.blit(card11, (i*100, playerHand.cardInHandDisplayY, 80,100))
        if whichCard == 12:
            screen.blit(card12, (i*100, playerHand.cardInHandDisplayY, 80,100))
        if whichCard == 13:
            screen.blit(card13, (i*100, playerHand.cardInHandDisplayY, 80,100))

def displaySelectedCards():
    for i in range(6):   
        selectedCard = p1.selectedToPlay[i]
        if selectedCard == 0:
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(i*100, playerHand.selectedCardY, 80, 100))
        if selectedCard == 2:
            screen.blit(card2, (i*100, playerHand.selectedCardY, 80,100))
        if selectedCard == 3:
            screen.blit(card3, (i*100, playerHand.selectedCardY, 80,100))
        if selectedCard == 4:
            screen.blit(card4, (i*100, playerHand.selectedCardY, 80,100))
        if selectedCard == 5:
            screen.blit(card5, (i*100, playerHand.selectedCardY, 80,100))
        if selectedCard == 6:
            screen.blit(card6, (i*100, playerHand.selectedCardY, 80,100))
        if selectedCard == 7:
            screen.blit(card7, (i*100, playerHand.selectedCardY, 80,100))
        if selectedCard == 8:
            screen.blit(card8, (i*100, playerHand.selectedCardY, 80,100))
        if selectedCard == 9:
            screen.blit(card9, (i*100, playerHand.selectedCardY, 80,100))
        if selectedCard == 10:
            screen.blit(card10, (i*100, playerHand.selectedCardY, 80,100))
        if selectedCard == 11:
            screen.blit(card11, (i*100, playerHand.selectedCardY, 80,100))
        if selectedCard == 12:
            screen.blit(card12, (i*100, playerHand.selectedCardY, 80,100))
        if selectedCard == 13:
            screen.blit(card13, (i*100, playerHand.selectedCardY, 80,100))

def displayCardsOnStack():
    for i in range(6):   
        selectedCard = p1.selectedToPlay[i]
        if selectedCard != 0:
             stack.stackDisplayX += 20
        if selectedCard == 2:
            screen.blit(card2, (stack.stackDisplayX, stack.stackDisplayY, 80,100))
        if selectedCard == 3:
            screen.blit(card3, (stack.stackDisplayX, stack.stackDisplayY, 80,100))
        if selectedCard == 4:
            screen.blit(card4, (stack.stackDisplayX, stack.stackDisplayY, 80,100))
        if selectedCard == 5:
            screen.blit(card5, (stack.stackDisplayX, stack.stackDisplayY, 80,100))
        if selectedCard == 6:
            screen.blit(card6, (stack.stackDisplayX, stack.stackDisplayY, 80,100))
        if selectedCard == 7:
            screen.blit(card7, (stack.stackDisplayX, stack.stackDisplayY, 80,100))
        if selectedCard == 8:
            screen.blit(card8, (stack.stackDisplayX, stack.stackDisplayY, 80,100))
        if selectedCard == 9:
            screen.blit(card9, (stack.stackDisplayX, stack.stackDisplayY, 80,100))
        if selectedCard == 10:
            screen.blit(card10, (stack.stackDisplayX, stack.stackDisplayY, 80,100))
        if selectedCard == 11:
            screen.blit(card11, (stack.stackDisplayX, stack.stackDisplayY, 80,100))
        if selectedCard == 12:
            screen.blit(card12, (stack.stackDisplayX, stack.stackDisplayY, 80,100))
        if selectedCard == 13:
            screen.blit(card13, (stack.stackDisplayX, stack.stackDisplayY, 80,100))

def clearStackDisplay():
    stack.stackDisplayX = 10
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 210, 800, 110))

def printPCplayerHand_forTesting():
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(10, 70, 800, 30))
    title = font.render("Opp hand (test):",True, (55,55,55))
    screen.blit(title, (10,70))
    for i in range(6):
        # hand
        blitTxt = font.render(str(p2.hand[i]),True, (55,55,55))
        screen.blit(blitTxt, ((i+4)*60,70))

def PCAi():
    noPossiblePlayPC = True
    p2.hand.sort()       # sortuje od najmniejszej wartosci zeby latwiej sprawdzac
    time.sleep(1)
    for i in range(6):   # sprawdz wsrod kart na rece
        if p2.hand[i] > stack.value:   # jesli najblizsza pojedyncza karta jest mniejsza od wartosci na stosie
            stack.count += 1          # wykonanie zagrania - zwieksz o 1 ilosc kart na stosie
            cardX = p2.hand[i]
            stack.value = p2.hand[i]   # ustal aktualna wartosc stosu na zagrana karte
            p2.hand[i] = shuffledDeck[0]   # uzupelnij brakujace miejsce na rece - dobierz karte
            shuffledDeck.pop(0)     # usun pierwsza karte z potasowanego decku - bo wlasnie ja PC dobral

            stack.stackDisplayX += 20
            screen.blit(globals()['card'+str(cardX)], (stack.stackDisplayX, stack.stackDisplayY, 80,100))
            noPossiblePlayPC = False # masz poprawne zagranie wiec wylacz pasowanie tury
            return
    for i in range(5):
        if p2.hand[i] == p2.hand[i+1]:    # jesli posortowane dwie kolejne karty sa rowne (warunek poprawnosci zagrania)
            twoCards = p2.hand[i] + p2.hand[i+1] # ich suma to wartosc zagrania
            if twoCards > stack.value:  # jesli ta suma wieksza od value na stosie
                stack.count += 2    # wykonanie zagrania - dwie karty na stos
                stack.value = twoCards   # wartosc stosu
                cardX = p2.hand[i]
                p2.hand[i] = shuffledDeck[0]     #  #
                shuffledDeck.pop(0)             #  #
                p2.hand[i+1] = shuffledDeck[0]   # dobierz dwie  jw. #
                shuffledDeck.pop(0)             # #

                stack.stackDisplayX += 20
                screen.blit(globals()['card'+str(cardX)], (stack.stackDisplayX, stack.stackDisplayY, 80,100))
                stack.stackDisplayX += 20
                screen.blit(globals()['card'+str(cardX)], (stack.stackDisplayX, stack.stackDisplayY, 80,100))
                noPossiblePlayPC = False # masz poprawne zagranie wiec wylacz pasowanie tury
                return
    if noPossiblePlayPC == True:
        p2.penaltyPoints += stack.count
        stack.value = 0
        stack.count = 0
        clearStackDisplay()
        p2.PCturn = PC_NO_PLAY

def checkCorrectPlay():
    correctPlay = True
    playPass = 0
    for i in range(6):  # sprawdz wszystkie sloty do zagrywania
        if p1.selectedToPlay[i] != 0:  # jesli w danym slocie jest wskazana karta
            wzor = p1.selectedToPlay[i]  # przypisz jej wartosc jako wzor (jesli wskazane wiecej to pozostanie ta ostatnia, jest to troche slabe) 
                                      # ale i tak maja byc wszystkie identyczne wiec chyba niewazne z czym porownamy
            for i in range(6): 
                if p1.selectedToPlay[i] != 0: # jesli slot nie jest pusty
                    if p1.selectedToPlay[i] != wzor: # i jesli nie jest taki jak wzor, czyli rozne wartosci 
                        correctPlay = False # zagranie jest nieprawidlowe

    # check if pass (no possible play)
    for i in range(6):
        if p1.selectedToPlay[i] == 0:
            playPass += 1

    if (p1.hand[0] == 0 and p1.hand[1] == 0 and p1.hand[2] == 0 and p1.hand[3] == 0 and p1.hand[4] == 0 and p1.hand[5] == 0):
        p1.penaltyPoints += stack.count
        stack.value = 0
        stack.count = 0
        select.count = 0
        playPass = 0
        p2.PCturn = True
        clearStackDisplay()
        
    
    if playPass == 6:
        p1.penaltyPoints += stack.count
        stack.value = 0
        stack.count = 0
        select.count = 0
        playPass = 0
        clearStackDisplay()
        #PCturn = True    # sprawdzic jak jest w zasadach, ale chyba ten co zebral zaczyna nowy ruch
        return
        
     
    if correctPlay == False:  
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(50, 130, 400, 60)) 
            blitTxt = font.render("Nieprawidlowe zagranie",True, (255,255,255))
            screen.blit(blitTxt, (50,130))
            incorrectPlayHandReset()
    elif correctPlay == True:
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(50, 130, 400, 60))
            blitTxt = font.render("Zajebiste zagranie stryjku",True, (255,255,255))
            screen.blit(blitTxt, (50,130))
            checkWithStackValue()
            

def checkWithStackValue():
    playValue = 0
    for i in range(6):
        playValue += p1.selectedToPlay[i]
    if playValue > stack.value:
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(50, 100, 500, 30))
        blitTxt = font.render("Zagrales za "+str(playValue)+" pkt.",True, (255,255,255))
        screen.blit(blitTxt, (50,100))
        stack.value = playValue
        stack.count = stack.count + select.count
        select.count = 0
        p2.PCturn = True
        displayCardsOnStack()
        discardPlayedCardsAndDraw()
    elif playValue <= stack.value:
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(50, 100, 200, 60))
        blitTxt = font.render("Za mala wartosc zagrania",True, (255,255,255))
        screen.blit(blitTxt, (50,100))
        incorrectPlayHandReset()    

def shuffleDeck():
    while len(baseDeck) != 0:       # shuffling the deck 
        wylosowany = random.randint(0, (len(baseDeck) - 1))
        shuffledDeck.append(baseDeck[wylosowany])
        baseDeck.pop(wylosowany)
    # adding 0's at the end of the deck - 'drawing empty cards' to check game over later
    for i in range (30):
        shuffledDeck.append(0)
    
def drawStartingHand():
    for i in range(6):
        p1.hand.append(shuffledDeck[0])
        shuffledDeck.pop(0)
        p2.hand.append(shuffledDeck[0])
        shuffledDeck.pop(0)

def printHand(lenght):
    for i in lenght:
        print(i,end =" ")

def selectCard():
    if p1.selectedToPlay[select.slot-1] == 0:
        p1.selectedToPlay[select.slot-1] = p1.hand[select.slot-1]
        p1.hand[select.slot-1] = 0
        select.count += 1
    elif p1.selectedToPlay[select.slot-1] != 0:
        p1.hand[select.slot-1] = p1.selectedToPlay[select.slot-1]
        p1.selectedToPlay[select.slot-1] = 0
        select.count -= 1

def incorrectPlayHandReset():
    for i in range(6):
        if p1.selectedToPlay[i] != 0:
            p1.hand[i] = p1.selectedToPlay[i]
            p1.selectedToPlay[i] = 0

def discardPlayedCardsAndDraw():
    for i in range(6):
        p1.selectedToPlay[i] = 0
        if p1.hand[i] == 0:
            p1.hand[i] = shuffledDeck[0]
            shuffledDeck.pop(0)

def gameOverCheck():
    global game, menu, gameover
    emptyHandCheck = 0
    for i in range(6):
        if p1.hand[i] == 0:
            emptyHandCheck += 1
    for i in range(6):
        if p2.hand[i] == 0:
            emptyHandCheck += 1
    if emptyHandCheck == 12:
        game = False
        gameover = True
        
    



while run == True:

# "MENU"
    clearScreen()
    cleanUpOnGameover()
    blitTxt = font.render("Tasuje decka, enter by zagrac",True, (255,255,255))
    screen.blit(blitTxt, (50,550))
    pygame.display.flip() 

    while menu == True:
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    clearScreen() 
                    menu = False
                    game = True
                    shuffleDeck()
                    drawStartingHand()
                    printHand(p1.hand)
                if event.key == pygame.K_ESCAPE:
                    menu = False
                    run = False





    

    while game == True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    select.slot = 1
                    selectCard()
                if event.key == pygame.K_2:
                    select.slot = 2
                    selectCard()
                if event.key == pygame.K_3:
                    select.slot = 3
                    selectCard()
                if event.key == pygame.K_4:
                    select.slot = 4
                    selectCard()
                if event.key == pygame.K_5:
                    select.slot = 5
                    selectCard()
                if event.key == pygame.K_6:
                    select.slot = 6
                    selectCard()
                #if event.key == pygame.K_a:   # Testing AI moves
                #    p2.PCturn = True
                if event.key == pygame.K_RETURN:
                    checkCorrectPlay()
                if event.key == pygame.K_ESCAPE:
                    game = False
                    menu = True
            displaySelectedCards()
            displayPlayerHand()
                
        displayHUDinfo()        
            
        
        if p2.PCturn == True:
            PCAi()
            if p2.PCturn == PC_NO_PLAY:
                PCAi()
            p2.PCturn = False

        
        printPCplayerHand_forTesting()
        gameOverCheck()
        pygame.display.flip()
        time.sleep(0.2)

    while gameover == True:
        clearScreen()
        blitTxt = font.render("Game over!",True, (255,255,255))
        blitTxt2 = font.render("Player penalty points = "+ str(p1.penaltyPoints),True, (255,255,255))
        blitTxt3 = font.render("PC penalty points = "+ str(p2.penaltyPoints),True, (255,255,255))

        if (p1.penaltyPoints < p2.penaltyPoints):
            blitTxt4 = font.render("YOU WIN !",True, (255,255,255))
        elif (p1.penaltyPoints > p2.penaltyPoints):
            blitTxt4 = font.render("YOU LOST !",True, (255,255,255))
        elif (p1.penaltyPoints == p2.penaltyPoints):
            blitTxt4 = font.render("STALEMATE !",True, (255,255,255))
        
        screen.blit(blitTxt, (50,50))
        screen.blit(blitTxt2, (50,150))
        screen.blit(blitTxt3, (50,250))
        screen.blit(blitTxt4, (50,350))
        
        pygame.display.flip() 

        time.sleep(1)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameover = False
                    menu = True
                if event.key == pygame.K_ESCAPE:
                    gameover = False
                    menu = True


    


        

        

    
        






