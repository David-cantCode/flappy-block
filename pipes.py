import pygame as py
import settings



class Pipe:

    def __init__(self, screen, screen_w, gap):
        self.screen = screen
        self.position_x = screen_w + 50
        self.gap = gap
        self.gap_size = 150
        self.speed =3 


    def move(self):
        self.position_x -= self.speed


    def draw(self, screen_h):
        #top
        py.draw.rect(self.screen, (0, 200, 0), (self.position_x, 0, settings.sqaure_size, self.gap - self.gap_size // 2))

        #bot
        py.draw.rect(self.screen, (0, 200, 0), (self.position_x, self.gap + self.gap_size // 2, settings.sqaure_size, screen_h))





    def is_off_screen(self):
        if self.position_x < -20:
            return True
        
        return False