import pygame

pygame.init()

SIZE = [600,600]

BLACK = [0, 0, 0]
BLUE = [150 ,150 ,255]
GREY = [112,113,114]
BROWN = [178, 125, 76]
WHITE = [255,255,255]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Animation")

done = False

clock = pygame.time.Clock()

#Variables
rect_x = 50


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")   
            print(pygame.mouse.get_pos())
            
    screen.fill(BLUE) 
    #BACKGROUND WITH BUILDINGS AND ROAD
    #ROAD
    pygame.draw.rect(screen, GREY , [0, 454, 1000, 300],0)
    pygame.draw.line(screen, WHITE, [20, 525], [100, 525], 5)
    pygame.draw.line(screen, WHITE, [120, 525], [200, 525], 5)
    pygame.draw.line(screen, WHITE, [220, 525], [300, 525], 5)
    pygame.draw.line(screen, WHITE, [320, 525], [400, 525], 5)
    pygame.draw.line(screen, WHITE, [420, 525], [500, 525], 5)
    #BUILDINGS
    pygame.draw.rect(screen, BROWN , [300, 454, 150, -200],0)
    pygame.draw.rect(screen, BROWN , [100, 454, 150, -400],0)
    
    
    #CAR
    pygame.draw.rect(screen, BLACK , [rect_x, 455, 250,100],0)
    pygame.draw.rect(screen, [255,255,255] , [rect_x + 50, 470, 50,50],0)
    pygame.draw.ellipse(screen, BLUE , [rect_x, 520, 50 ,50],0)
    pygame.draw.ellipse(screen, BLUE , [rect_x + 200, 520, 50 ,50],0)
    
    
    rect_x += 5
    if rect_x > 620:
      rect_x = -400    
    
    
    pygame.display.flip()
    
    clock.tick(60)
            
pygame.quit()            