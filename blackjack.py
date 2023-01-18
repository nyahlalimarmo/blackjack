import time
import random

class Player:

    def __init__(self, n):
        self.name = n
        self.handValue = 0
        self.hand = []

    def __str__(self):
        return(self.name)

    def updateHandValue(handValue, card, cardValue):
        #input: player's handvalue, the card theyre dealt, and the BJ value of that card
        #process: adds the new value to the handvalue
        #unless card is an Ace; then 11 or 1 (if +11 would make > 21)
        #output: new handvalue
        if not card.startswith("Ace"):
            return handValue + cardValue
        elif handValue > 10:
            return handValue + cardValue
        else:
            return handValue + 11

    def displayHand(self):
        #input: self
        #process: pretty prints player's hand
        #output: hand list in a column (one card each)
        print(*self.hand, sep='\n')
        

def instructions():
    #input: none
    #process: print instructions and welcome statement
    #output: instructions
    print("Welcome to BlackJack!")
    time.sleep(2)
    print("The rules are simple: I start you off with two cards each")
    print("and you will add up the value of your cards.")
    time.sleep(4)
    print("Once you add what's in your hand, you will tell me whether you want")
    print("to hit or stand, meaning get another card or just stay as you are.")
    time.sleep(5)
    print("Your goal is to get as close to 21 as you can without going over.")
    time.sleep(2)
    print("Some reminders: Player 2 is automatically the dealer; Ace can be both 1 and 11 and the royals = 11.")
    time.sleep(3)
    print("Good luck!")


def createDeck():
    #input: none
    #process: creates a deck of cards as a dictionary by going through all combinations of suits and values
    #output: the deck as a dictionary
    suits = ['♦', '♥', '♣', '♠']
    royals = {'Ace': 1, 'King': 11, 'Queen': 11, 'Jack': 11}

    numbers = ['Ace', 'King', 'Queen', 'Jack']
    for i in range(2,11):
        numbers.append(str(i))

    deck = {}
    for s in suits:
        for num in numbers:
            if num.isnumeric():
                deck[num + ' of ' + s] = int(num)
            else:
                deck[num + ' of ' + s] = royals[num]
    return deck


def deal(deck):
    #input: deck dictionary
    #process: takes keys from deck dictionary, shuffle them, then takes 1 from that
    #becoming value of the card
    #output: returns the key and value pair - this is the card dealt
    keys = list(deck.keys())
    random.shuffle(keys)
    value = deck.pop(keys[0])
    return (keys[0], value)


def HitOrStay(p1, deck, hv):
    #input: player 1, deck, player 1's hand value
    #process: p1 asked if wants to hit or stay, if hit, dealt another card
    #this card is aded to their hand and their hand value is recalculated
    #output: new hand value
    p1more = input("Player 1, do you want to hit or stay? hit/stay: ")

    if p1more == "hit":
        p1hit_card, p1hit_value = deal(deck)
        hv = Player.updateHandValue(hv, p1hit_card, p1hit_value)
        p1.hand.append(p1hit_card)
        print(p1, 'was dealt', p1hit_card)
    
    return hv


def dealerHitOrStay(p2, deck, hv):
    #input: player 2, deck, playeer 2 handvalue
    #process: dealer is dealt another card if their handvalue was less than or equal to 16
    #if they're dealt a new card, hand value is recalculated
    #output: new hand value
    if hv <= 16:
        card, value = deal(deck)
        hv = Player.updateHandValue(hv, card, value)
        p2.hand.append(card)
        print("The dealer,", p2, "was dealt", card)
    
    return hv


def main():
    #main function
    instructions()
    player1name = input("Player 1, what is your name? ")
    player2name = input("Player 2, what is your name? You are the dealer. ")
    player1 = Player(player1name)
    dealer = Player(player2name)
    deck = createDeck()
    handvalue1 = 0
    handvalue2 = 0

    for x in range(2):
        card, value = deal(deck)
        handvalue1 = Player.updateHandValue(handvalue1, card, value)
        player1.hand.append(card)
        print(player1, 'was dealt', card)

        card, value = deal(deck)
        handvalue2 = Player.updateHandValue(handvalue2, card, value)
        dealer.hand.append(card)
        print(dealer , 'was dealt', card)
        print()

    handvalue1 = HitOrStay(player1, deck, handvalue1)
    handvalue2 = dealerHitOrStay(dealer, deck, handvalue2)


    if handvalue1 > 21 and handvalue2 > 21:                    #both bust
        print("Bust! Both of you lose! :( ")
        print(player1, "'s hand was: ")
        player1.displayHand()
        print(dealer, "'s hand was: ")
        dealer.displayHand()
    elif handvalue1 == handvalue2:                                  #same value
        print("You have the same number! You both lose.")
        print(player1, "'s hand was: ")
        player1.displayHand()
        print(dealer, "'s hand was: ")
        dealer.displayHand()
    elif handvalue1 > 21:                                             #p1 bust
        print(player1, ", that's a bust!", dealer, "you win!!")
        print(player1, "'s hand was: ")
        player1.displayHand()
        print(dealer, "'s hand was: ")
        dealer.displayHand()
    elif handvalue2 > 21:                                               #p2 bust
        print(dealer, ", that's a bust!", player1, "you win!!")
        print(player1, "'s hand was: ")
        player1.displayHand()
        print(dealer, "'s hand was: ")
        dealer.displayHand()
    elif handvalue1 > handvalue2 and handvalue1 < 21:                  #p1 win, greater than p2's
        print(player1, ", you win!!")
        print(player1, "'s hand was: ")
        player1.displayHand()
        print(dealer, "'s hand was: ")
        dealer.displayHand()
    else:                                                             #p2 win, greater than p1's
        print(dealer, ", you win!!")
        print(player1, "'s hand was: ")
        player1.displayHand()
        print(dealer, "'s hand was: ")
        dealer.displayHand()



main()