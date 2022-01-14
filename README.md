*** Szkola Pythonowania ***

1. Introduction
	
	Szkola Pythonowania (The School of Pythoning) is a simple card game using the basic mechanics from card game "Szkola Latania".
	Written to practice programming in Python. Pygame used. "Funny" placeholder graphics made by myself in MS Paint.
	
	
2.	Controls

	First you'll see the 'menu' screen, wait a second or two while the deck is shuffling, then press Enter.
	Then you'll see the 'game' screen - contents of your hand on bottom, and basic info up the screen.
	Select cards to play by pressing 1 to 6 on your keyboard, you will notice the card moves up - it's selected to play.
	Confirm your play after selecting cards with pressing Enter.
	The play that is aginst the rules will be alerted and ypur selection will be cleared so you can play correctly.
	If you have no possible play (or prefer to pass), press Enter without selecting any cards, you will take the cards from stack
	and earn penalty points.
	
3.  Rules

	Players play cards on stack, each card have a value nuber. Each player has to make play with higher value than is already on stack.
	Player who can't play higher must take cards from the stack, the amount of cards is added to that player's penalty points.
	Game goes on until no player have cards in hand. At the end, player with higher penalty points loses the game.
	You can play single cards, pairs, trios etc., but the cards must have equal value.
	Example: there's 8 on stack - you can play 3+3=3 to get 9, or 6+6 to get 12, but you can't play 5+6 to get 11.
	
4. Requirements
	
	Pygame.
	cmd - python SzkolaPythonowania.py

