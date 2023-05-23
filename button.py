import pygame.font

class Button:
    """class to create buttons for the game"""
    def __init__(self, ai_game, msg) -> None:
        #get surface
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        #button properties
        self.width, self.height = 200, 50
        self.color = (135, 135, 135)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        #create button rect
        self.rect = pygame.Rect((0, 0), (self.width, self.height))
        #center button
        self.rect.center = self.screen_rect.center
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turns msg into an image and centers it on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """draw a blank button and then """
        #draw blank button
        self.screen.fill(self.color, self.rect)
        #place text image in it
        self.screen.blit(self.msg_image, self.msg_image_rect)


         