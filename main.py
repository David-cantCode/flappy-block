import pygame as py 
import settings 
import map
import player as p 


screen_w =  settings.sqaure_size * map.cols
screen_h =  settings.sqaure_size * map.rows



screen = py.display.set_mode((screen_w, screen_h))
py.display.set_caption("flappy block ") 
clock  = py.time.Clock()



player = p.Player(screen  , (200, (screen_h /2)) )



running = True
while running:
    screen.fill((0, 0, 0)) 

    for event in py.event.get():
        if event.type == py.QUIT: 
            running = False

        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                player.jump()
    




    player.draw()
    player.move()
    
    
    
    
    
    py.display.flip() 
    clock.tick(settings.fps)
    