import pygame as py
import settings

class Player:
    def __init__(self,screen, position):
        self.screen = screen
        self.position = list(position)  
        self.velocity = 0
        self.gravity = 0.5       
        self.jump_force = -8     
        self.max_fall_speed = 10




    def move(self):

        # apply gravity
        self.velocity += self.gravity
        if self.velocity > self.max_fall_speed:
            self.velocity = self.max_fall_speed




        self.position[1] += self.velocity


    def draw(self):
        py.draw.rect(self.screen, (140,0,250), (self.position[0], self.position[1], settings.sqaure_size, settings.sqaure_size))


        print(f" Pos: {self.position[0]} , {self.position[1]}")
 



    def jump(self):
        self.velocity = self.jump_force