import pygame

class Card():
    def __init__(self, image):
        self.sheet = image

    def getCardBack(self, style, width, height, scale, color):

        # Change the color of the card based on which style was selected.
        if style == 1:
            pos_x = 0
            pos_y = 0
        elif style == 2:
            pos_x = 1
            pos_y = 0
        elif style == 3:
            pos_x = 2
            pos_y = 0

        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((pos_x * width), (pos_y * height), width, height))

        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        

        return image

    def getCardfront(self, rank, suit, width, height, scale, color):
        # Determine frameX and frameY based on the rank and suit
        if suit == 'S':
            if rank == 'Q':
                frameX = 0
                frameY = 0
            elif rank == 'K':
                frameX = 0
                frameY = 1
            elif rank == 'J':
                frameX = 0
                frameY = 2
            elif rank == 'A':
                frameX = 0
                frameY = 3
            elif rank == '10':
                frameX = 0
                frameY = 4
            elif rank == '9':
                frameX = 0
                frameY = 5
            elif rank == '8':
                frameX = 0
                frameY = 6
            elif rank == '7':
                frameX = 0
                frameY = 7
            elif rank == '6':
                frameX = 0
                frameY = 8
            elif rank == '5':
                frameX = 0
                frameY = 9
            elif rank == '4':
                frameX = 1
                frameY = 0
            elif rank == '3':
                frameX = 1
                frameY = 1
            elif rank == '2':
                frameX = 1
                frameY = 2
        elif suit == 'H':
            # do stuff
            if rank == 'Q':
                frameX = 1
                frameY = 4
            elif rank == 'K':
                frameX = 1
                frameY = 5
            elif rank == 'J':
                frameX = 1
                frameY = 6
            elif rank == 'A':
                frameX = 1
                frameY = 7
            elif rank == '10':
                frameX = 1
                frameY = 8
            elif rank == '9':
                frameX = 1
                frameY = 9
            elif rank == '8':
                frameX = 2
                frameY = 0
            elif rank == '7':
                frameX = 2
                frameY = 1
            elif rank == '6':
                frameX = 2
                frameY = 2
            elif rank == '5':
                frameX = 2
                frameY = 3
            elif rank == '4':
                frameX = 2
                frameY = 4
            elif rank == '3':
                frameX = 2
                frameY = 5
            elif rank == '2':
                frameX = 5
                frameY = 2
            
        elif suit == 'D':
            if rank == 'Q':
                frameX = 2
                frameY = 7
            elif rank == 'K':
                frameX = 2
                frameY = 8
            elif rank == 'J':
                frameX = 2
                frameY = 9
            elif rank == 'A':
                frameX = 3
                frameY = 0
            elif rank == '10':
                frameX = 3
                frameY = 1
            elif rank == '9':
                frameX = 3
                frameY = 2
            elif rank == '8':
                frameX = 3
                frameY = 3
            elif rank == '7':
                frameX = 3
                frameY = 4
            elif rank == '6':
                frameX = 3
                frameY = 5
            elif rank == '5':
                frameX = 3
                frameY = 6
            elif rank == '4':
                frameX = 3
                frameY = 7
            elif rank == '3':
                frameX = 3
                frameY = 8
            elif rank == '2':
                frameX = 3
                frameY = 9
        elif suit == 'C':
            if rank == 'Q':
                frameX = 4
                frameY = 0
            elif rank == 'K':
                frameX = 4
                frameY = 1
            elif rank == 'J':
                frameX = 4
                frameY = 2
            elif rank == 'A':
                frameX = 4
                frameY = 3
            elif rank == '10':
                frameX = 4
                frameY = 4
            elif rank == '9':
                frameX = 4
                frameY = 5
            elif rank == '8':
                frameX = 4
                frameY = 6
            elif rank == '7':
                frameX = 4
                frameY = 7
            elif rank == '6':
                frameX = 4
                frameY = 8
            elif rank == '5':
                frameX = 4
                frameY = 9
            elif rank == '4':
                frameX = 5
                frameY = 0
            elif rank == '3':
                frameX = 5
                frameY = 1
            elif rank == '2':
                frameX = 2
                frameY = 6
        
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frameX * width), (frameY * height), width, height))

        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        

        return image
    
    def getCardValue(self, card_value):

        try:
            value = int(card_value)
            return value
        
        except ValueError:
            # Handle the case where card_value is not a valid integer
            print(f"Error: {card_value} is not a valid integer")
            
            return None