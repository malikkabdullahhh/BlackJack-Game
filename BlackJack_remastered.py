import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')
values = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'jack':10, 'queen':10, 'king':10, 'ace':11}

playing = True


class Card:

	def __init__(self,rank,suit):
		self.rank = rank
		self.suit = suit

	def __str__(self):
		return(self.rank + ' of ' + self.suit)

class Deck:

	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(rank,suit))

	def __str__(self):
		deck_cards=''
		for card in self.deck:
			deck_cards+='\n'+ card.__str__()
		return "The cards in Deck are: \n"+deck_cards

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		single_card = self.deck.pop()
		return single_card

class Hand:

	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self,card):
		self.cards.append(card)
		self.value += values[card.rank]

		if card.rank == "ace":
			self.aces += 1

	def adjust_for_ace(self):
		while self.value > 21 and self.aces:
			self.value -= 10
			self.aces -= 1


class Chips:

	def __init__(self,total):
		self.total = total
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet




def take_bet(chips):

	while True:

		try:
			chips.bet = int(input("How many chips would you like to bet? "))
		except:
			print("Sorry please provide an integer")
		else:
			if chips.bet > chips.total:
				print("Sorry, you do not have enough chips! You have {}".format(chips.total))
			else:
				break


def hit(deck,hand):
	hand.add_card(deck.deal())
	hand.adjust_for_ace()

def hit_or_stand(deck,hand):
	global playing

	while True:
		x = input("\nHit or Stand? Enter h/s ")

		if x[0].lower()=='h':
			hit(deck,hand)

		elif x[0].lower()=='s':
			print("\nPlayer Stands, Dealer's Turn\n")
			playing = False
		else:
			print("Sorry, I did not understand that, Please enter h or s only! ")
			continue

		break

#visual representation of the hands

def show_some(player,dealer):
	print("\nDEALER'S HAND: ")
	print("*hidden card* \n"+str(dealer.cards[1]))
	print("\nPLAYER'S HAND: ")
	for card in player.cards:
		print(card)

def show_all(player,dealer):
	print("DEALER'S HAND: ")
	for card in dealer.cards:
		print(card)
	print("\n")
	print("PLAYER'S HAND")
	for card in player.cards:
		print(card)

#different scenarios....

def player_busts(player,dealer,chips):
	print("PLAYER HAS BUSTED!")
	chips.lose_bet()

def player_wins(player,dealer,chips):
	print("PLAYER WINS!")
	chips.win_bet()

def dealer_busts(player,dealer,chips):
	print("DEALER HAS BUSTED!")
	chips.win_bet()

def dealer_wins(player,dealer,chips):
	print("DEALER WINS!")
	chips.lose_bet()

def push(player,dealer):
	print("Dealer and Player tie! *PUSH*")


#On to the Game itself...
play=1

while True:
	try:
		budget = int(input("Enter your gambling budget: "))
		break
	except:
		print("please enter a valid amount")

while True:
	print("\nWelcome to BlackJack Fellas")

	deck = Deck()
	deck.shuffle()

	dealer_hand = Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

	player_hand = Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())


	if play==1:
		player_chips = Chips(budget)

	take_bet(player_chips)


	while playing:

		show_some(player_hand,dealer_hand)

		hit_or_stand(deck,player_hand)


		if player_hand.value > 21:
			player_busts(player_hand,dealer_hand,player_chips)
			break
	input("\nEnter any key to reveal dealer's hand ")
	show_all(player_hand,dealer_hand)

	if player_hand.value <= 21:

		while dealer_hand.value < player_hand.value:
			hit(deck,dealer_hand)
			input("\nEnter any key to observe dealer's move ")
			show_all(player_hand,dealer_hand)

		if dealer_hand.value > 21:
			dealer_busts(player_hand,dealer_hand,player_chips)

		elif dealer_hand.value > player_hand.value:
			dealer_wins(player_hand,dealer_hand,player_chips)

		elif dealer_hand.value < player_hand.value:
			player_wins(player_hand,dealer_hand,player_chips)

		else:
			push(player_hand,dealer_hand)

	print("\nPlayer's winnings stand at ",player_chips.total)
	input("\npress any key to proceed...")

	#another game....

	if player_chips.total==0:
		print("\nSorry, you do not have enough chips to play another hand!")
		break

	new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

	if new_game[0].lower()=='y':
		playing = True
		print("\n")
		play+=1
		continue

	else:
		print("Thanks for playing!")
		break










