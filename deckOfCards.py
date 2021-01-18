import itertools
import random

class node:
    def __init__(self,rank,card):
        self.rank=rank
        self.card=card
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None

    def printLinkedList(self):
        temp=self.head
        while(temp):
            if temp.rank=="1000":
                print("Ace of "+temp.card)
            elif temp.rank=="995":
                print("King of "+temp.card)
            elif temp.rank=="990":
                print("Queen of "+temp.card)
            elif temp.rank=="900":
                print("Jack of "+temp.card)
            else:
                print(temp.rank+" Of "+temp.card)
            temp=temp.next
  
        

class deckOfCards:

    def distributeCards(self,cards,playerCards):
        rank = []
        temp=playerCards.head
        for index in range(9):
            rank.append(cards[index][0])
            
            if(not temp):
                playerCards.head=node(rank[index],cards[index][1])
                temp=playerCards.head
            else:
                while(temp):
                    if(not temp.next):
                        temp.next=node(rank[index],cards[index][1])
                        break
                temp=temp.next

            cards.remove(cards[index])

        return playerCards,cards
        

    def shuffleDeck(self):
        cards = list(itertools.product([ "2", "3", "4", "5", "6", "7", "8", "9", "10", "900", "990", "995", "1000"],
                              ['Clubs', 'Diamonds', 'Hearts', 'Spades']))

        random.shuffle(cards)

        return cards

if __name__ == "__main__":
    player1cards=linkedList()
    player2cards=linkedList()
    player3cards=linkedList()
    player4cards=linkedList()
    deckObj=deckOfCards()
    cards=deckObj.shuffleDeck()
    player1cards,cards=deckObj.distributeCards(cards,player1cards)
    player2cards,cards=deckObj.distributeCards(cards,player2cards)
    player3cards,cards=deckObj.distributeCards(cards,player3cards)
    player4cards,cards=deckObj.distributeCards(cards,player4cards)

    print("\nplayer 1 cards:\n")
    player1cards.printLinkedList()
    print("\nplayer 2 cards:\n")
    player2cards.printLinkedList()
    print("\nplayer 3 cards:\n")
    player3cards.printLinkedList()
    print("\nplayer 4 cards:\n")
    player4cards.printLinkedList()