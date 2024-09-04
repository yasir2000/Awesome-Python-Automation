import random
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Card:
    """Represents a playing card."""
    def __init__(self, value):
        self.value = value

class Deck:
    """Represents a deck of playing cards."""
    def __init__(self):
        self.cards = []
        self.gen_deck()

    def gen_deck(self):
        for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
            self.cards.extend([Card(value) for _ in range(4)])  # Four cards of each type

    def draw(self):
        return self.cards.pop(random.randint(0, len(self.cards) - 1))

class Player:
    """Represents a player in the game."""
    def __init__(self, name, age, player_type, initial_money=1000):
        self.name = name
        self.age = age
        self.cards = []
        self.score = 0
        self.money = initial_money
        self.bet = 0
        self.score_dictionary = self.create_score_dictionary()

    @staticmethod
    def create_score_dictionary():
        return {str(i): i for i in range(2, 11)} | {face: 10 for face in ['J', 'Q', 'K']} | {'A': 11}

    def place_bet(self):
        min_bet = os.getenv("MIN_BET", 5)
        max_bet = os.getenv("MAX_BET", 100)

        while True:
            try:
                bet = int(input(f"Enter your bet amount ({min_bet}-{max_bet}): "))
                if bet < min_bet or bet > max_bet or bet > self.money:
                    print("Invalid bet amount. Please try again.")
                else:
                    self.bet = bet
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def draw_card(self, card):
        self.cards.append(card)
        self.update_score()

    def update_score(self):
        self.score = sum(self.score_dictionary[card.value] for card in self.cards)
        self.adjust_ace_value()

    def adjust_ace_value(self):
        while self.score > 21 and any(card.value == 'A' for card in self.cards):
            self.score -= 10

class Dealer(Player):
    """Represents the dealer in the game."""
    def __init__(self, name):
        super().__init__(name, 0, 'AI')

class GameBlackJack:
    """Represents the Blackjack game."""
    def __init__(self, dealer, players):
        self.dealer = dealer
        self.players = players
        self.deck = Deck()

    def start_round(self):
        for player in self.players:
            player.place_bet()

    def deal_initial_cards(self):
        for _ in range(2):  # Deal two cards to each player and dealer
            for player in self.players:
                player.draw_card(self.deck.draw())
            self.dealer.draw_card(self.deck.draw())

    def play_round(self):
        for player in self.players:
            if isinstance(player, Player):  # If the player is a human
                self.player_turn(player)

        self.dealer_turn()  # Dealer plays after all players

    def player_turn(self, player):
        while player.score < 21:
            choice = input(f"{player.name}, do you want to draw another card? (yes/no) ").strip().lower()
            if choice == 'yes':
                player.draw_card(self.deck.draw())
                print(f"{player.name}'s cards: {[card.value for card in player.cards]} - Score: {player.score}")
            elif choice == 'no':
                break

    def dealer_turn(self):
        while self.dealer.score < 17:  # Dealer must hit until at least 17
            self.dealer.draw_card(self.deck.draw())
        print(f"Dealer's cards: {[card.value for card in self.dealer.cards]} - Score: {self.dealer.score}")

    def determine_winner(self):
        for player in self.players:
            if player.score <= 21:
                if self.dealer.score > 21 or player.score > self.dealer.score:
                    player.money += player.bet  # Player wins
                    print(f"{player.name} wins!")
                elif player.score < self.dealer.score:
                    player.money -= player.bet  # Dealer wins
                    print(f"{player.name} loses to the dealer.")
                else:
                    print(f"{player.name} and dealer tie.")

    def remove_losers(self):
        self.players = [player for player in self.players if player.money > 0]

# Load environment variables
min_bet = os.getenv("MIN_BET", 5)
max_bet = os.getenv("MAX_BET", 100)

# Initialize players and dealer
players = [Player('George', 22, 'human'), Player('soon', 21, 'AI'), Player('PAXI', 28, 'AI'), Player('cactus', 41, 'AI')]
dealer = Dealer('Mc Donald')

# Start game
game = GameBlackJack(dealer, players)
num_rounds = 2

for round_num in range(num_rounds):
    print(f"Round {round_num + 1} starts!")
    game.start_round()
    game.deal_initial_cards()
    game.play_round()
    game.determine_winner()
    game.remove_losers()
