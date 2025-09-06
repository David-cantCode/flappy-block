import pygame as py 
import settings 
import map

screen_w =  settings.sqaure_size * map.cols
screen_h =  settings.sqaure_size * map.rows



screen = py.display.set_mode((screen_w, screen_h))
py.display.set_caption("flappy block ") 
clock  = py.time.Clock()



running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT: 
            running = False


    
    
    
    
    
    screen.fill((0, 0, 0)) 
    py.display.flip() 
    clock.tick(settings.fps)
    