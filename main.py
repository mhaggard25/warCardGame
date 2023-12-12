# War card game
# Created by: Matt Haggard
# Version: 0.1

# imports
import pygame, itertools, random

# build the deck
cardValues = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A' ]
cardSuits = ['S', 'H', 'C', 'D']

deck = list(itertools.product(cardValues, cardSuits))

# shuffle the deck (I'll have to do this when the game starts.)
random.shuffle(deck)

# Debug
#for value, suit in deck:
#    print('the %s of %s' % (value, suit))

# Making sure that I can access
#print("Here is the second card in the deck" , deck[1])
#print("Here is the Value of the second card in the deck", deck[1][0])

# make player hands
player1Hand = []
player2Hand = []

# put cards in player hands after shuffle 
for card in range(0, len(deck), 2):
    player1Hand.append(deck[card])

for card in range(1, len(deck), 2):
    player2Hand.append(deck[card])


# print both hands for debug
print('\nPlayer 1 hand:')
for element in player1Hand:
    print(element)

print('\nPlayer 2 hand: ')
for element in player2Hand:
    print(element)

# print the length of both hands for more debug
print('player1 hand length:', len(player1Hand))
print('player2 hand length:', len(player2Hand))


#TODO: build the gameplay logic (what beats what, tie breakers, etc)
#TODO: User input (mouse, keyboard, controller?)
#TODO: import the card images and assign them to specific cards
#TODO: Build the gameplay area
#TODO: keep score and display
#TODO: end game
#TODO: Build the menu
#TODO: Build settings menu
#TODO: other graphics (maybe throw some tanks in there or a word that says "WAR" during a tie or something.)
#TODO: record keeping


"""

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Load some images
background = pygame.image.load("background.jpg")


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

    # flip() the display to put work on screen
    pygame.display.flip()

    # limit display to 60 fps
    clock.tick(60)

pygame.quit()

"""