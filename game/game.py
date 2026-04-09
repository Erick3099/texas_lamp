from Deck import Deck 
from player import player

class Game ():
    def __init__(self):
        self.main_pot=0
        self.current_pot=0
        deck=Deck()
        deck.shuffle()
        deck.shuffle()
        human_cards= [deck.give_card(),deck.give_card()]
        pc_card=[deck.give_card(),deck.give_card()]
        #chess engine draw:

        self.human=player(type="human",
                          cards=human_cards,
                          total_amount_bet=0,
                          name="Erick",amount=2000)
        self.pc=player(type="pc",
                       cards=pc_card,
                       total_amount_bet=0,
                       name="Erick",amount=2000)
        self.deck=deck

if __name__=="__main__":
    game=Game()
    game.deck.print_deck()
    print("This is the deck")
    print("pc cards")
    game.pc.cards[0].print_card()
    game.pc.cards[1].print_card()
    print("This is the deck")
    print("Human cards")
    game.human.cards[0].print_cards()
    game.human.cards[1].print_cards