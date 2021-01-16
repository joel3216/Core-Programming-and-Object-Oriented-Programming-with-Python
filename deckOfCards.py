import itertools
import random



class deckOfCards:

    def distributeCards(self,cards):
        players=[[]]
        for i in range(1,5):
            print("player "+str(i))
            rank = []
            for index in range(9):
                rank.append(cards[index][0])
                players[i-1].append(rank[index]+" of "+cards[index][1])
                cards.remove(cards[index])
            print(players[i-1])
            print("\n")
            players.append([])

    def shuffleDeck(self):
        cards = list(itertools.product([ "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"],
                              ['Clubs', 'Diamonds', 'Hearts', 'Spades']))

        random.shuffle(cards)

        self.distributeCards(cards)

if __name__ == "__main__":
    deckObj=deckOfCards()
    deckObj.shuffleDeck()  