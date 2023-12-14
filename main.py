# War card game
# Created by: Matt Haggard
# Version: 0.1

# imports
import pygame, itertools, random
import card

#TODO: build the gameplay logic (what beats what, tie breakers, etc)
#TODO: User input (mouse, keyboard, controller?)
#TODO: Build the gameplay area
#TODO: keep score and display
#TODO: end game
#TODO: Build the menu
#TODO: Build settings menu
#TODO: other graphics (maybe throw some tanks in there or a word that says "WAR" during a tie or something.)
#TODO: record keeping

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('War - The Card Game')
clock = pygame.time.Clock()
running = True

# Load game images
background = pygame.image.load("background.jpg")
spriteSheetFront = pygame.image.load('playingCards.png').convert_alpha()
spriteSheetBack = pygame.image.load('playingCardBacks.png').convert_alpha()

card_sprite_sheet = card.Card(spriteSheetFront)
card_backs_sprite_sheet = card.Card(spriteSheetBack)

# Set the variables for the size of the card and the transparency
cardWidth = 140
cardHeight = 190
black = 0, 0, 0


# Testing to ensure that the images load correctly
#frame0 = card_sprite_sheet.getCardFront('Q', 'H', cardWidth, cardHeight, 1, black)
#frame1 = card_sprite_sheet.getCardFront(1, 1,  cardWidth, cardHeight, 1, black)
#frame2 = card_sprite_sheet.getCardFront(2, 2, cardWidth, cardHeight, 1, black)
#frame3 = card_sprite_sheet.getCardFront(3, 3, cardWidth, cardHeight, 1, black)

# build the deck
# put the cards in the order that they are in on the image so that it loads in correctly without much effort
cardValues = ['Q', 'K', 'J', 'A', '10', '9', '8', '7', '6', '5', '4', '3', '2' ]
cardSuits = ['S', 'H', 'D', 'C']

#deck = [list(itertools.product(cardValues, cardSuits))]

# read into a tuple the card information and build the deck.
deck = [(rank, suit, card_sprite_sheet.getCardfront(rank, suit, cardWidth, cardHeight, 1, black)) 
        for rank, suit in itertools.product(cardValues, cardSuits)]

# shuffle the deck (I'll have to do this when the game starts.)
random.shuffle(deck)

# Debug
#for value, suit in deck:
#    print('the %s of %s' % (value, suit))

# Making sure that I can access
#print("Here is the second card in the deck" , deck[0])
#print("Here is the Value of the second card in the deck", deck[0][0])


# make player hands
player1Hand = []
player2Hand = []

# put cards in player hands after shuffle 
for card_index in range(0, len(deck), 2):
    player1Hand.append(deck[card_index])

for card_index in range(1, len(deck), 2):
    player2Hand.append(deck[card_index])


# print both hands for debug
"""
print('\nPlayer 1 hand:')
for element in player1Hand:
    print(element)

print('\nPlayer 2 hand: ')
for element in player2Hand:
    print(element)
"""


# print the length of both hands for more debug
#print('player1 hand length:', len(player1Hand))
#print('player2 hand length:', len(player2Hand))


while running:
    # poll for events
    # pygame.QUIT means that the user clicked the X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color
    screen.fill("purple")
    
    # render the game here
    screen.blit(background, (0, 0))

    # DEBUG: Display player1's hand
    """
    player1_x, player1_y = 10, 10
    spacing = 20  # Spacing between cards
    for card_index, card_info in enumerate(player1Hand):
        card_x = player1_x + card_index * (cardWidth + spacing)
        card_y = player1_y
        screen.blit(card_info[2], (card_x, card_y))
        """
    
    # This shows the player's deck while they still have cards in it. 
    screen.blit(card.Card.getCardBack(card_backs_sprite_sheet, 1, cardWidth, cardHeight, 1, black), (10, 520))

    # This shows player two's deck while they still have cards in it. 
    screen.blit(card.Card.getCardBack(card_backs_sprite_sheet, 1, cardWidth, cardHeight, 1, black), (1270 - cardWidth, 10))

    # This is where player one will "play" their card when they play it. 
    # For now it just shows the first card in the players hand. 
    screen.blit(player1Hand[0][2], (400, 300))

    # This is player two's card that they have played
    # for now it just shows the first card in their hand.
    screen.blit(player2Hand[0][2], (880 - cardWidth, 300))


    # flip() the display to put work on screen
    pygame.display.flip()


    # limit display to 60 fps
    clock.tick(60)

pygame.quit()