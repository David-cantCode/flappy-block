import pygame as py 
import settings 
import map
import player as p 
import random as rn
import pipes as pipe_class

screen_w =  settings.sqaure_size * map.cols
screen_h =  settings.sqaure_size * map.rows



screen = py.display.set_mode((screen_w, screen_h))
py.display.set_caption("flappy block ") 
clock  = py.time.Clock()



player = p.Player(screen  , (200, (screen_h /2)) )


pipes = []
pipe_timer = 50
pipe_interval = 90 






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
    



    #pipes

    if pipe_timer > pipe_interval:
        pipe_timer = 0
        gap_pos =  rn.randint(100, screen_h - 100)
        pipes.append(pipe_class.Pipe(screen, screen_w, gap_pos))



    for pipe in pipes[:]:
        pipe.move()
        pipe.draw(screen_h)
        if pipe.is_off_screen():
            pipes.remove(pipe)



    pipe_timer += 1
    
    
    py.display.flip() 
    clock.tick(settings.fps)
    