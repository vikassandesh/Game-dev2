import pygame
# to set the dimesions of the scrren in pygame
screen = pygame.display.set_mode((600,600))

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (0,0,0)

screen.fill(white)


class rectangle():
    def __init__(self,color,dimensions):              # constructer- to intialize variables
        self.rect_surf = screen
        self.rect_color = color
        self.rect_dim = dimensions
        
    def draw(self): 
        self.Draw_Rect = pygame.draw.rect(self.rect_surf,
                                          self.rect_color,
                                          self.rect_dim
                                          )
        