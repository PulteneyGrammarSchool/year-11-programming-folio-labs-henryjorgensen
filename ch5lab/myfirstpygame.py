import pygame
pygame.init()
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
LIGHTGREEN = (37, 237, 160)
YELLOW = (255, 221, 0)
LIGHTBLUE = (217, 229, 249)

PI = 3.141592

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Henry's Cool Game")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT:
            print("User asked to quit.")
            done = True
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")   
            print(pygame.mouse.get_pos())
 
    # --- Game logic should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(LIGHTBLUE)

    pygame.draw.rect(screen, BLUE, [50, 450, 600, -300], 5)
    pygame.draw.rect(screen, GREEN, [0, 454, 1000, 300], 0)
    pygame.draw.rect(screen, BLUE, [309, 448, 50, -80], 0)
    pygame.draw.ellipse(screen, YELLOW , [349,400,10,10], )
      
    
    
    for x_offset in range(0, 600, 200):
       pygame.draw.rect(screen, BLUE, [139 + x_offset, 194, 80, 80], 5) #creates window
    
    #pygame.draw.line(screen, GREEN, [20, 20], [100, 20], 5)
    #pygame.draw.line(screen, GREEN, [100, 20], [100, 150], 5)
    #pygame.draw.line(screen, GREEN, [100, 150], [20, 150], 5)
    #pygame.draw.line(screen, GREEN, [20, 150], [20, 20], 5)
    
    pygame.draw.ellipse(screen, YELLOW , [20,20,100,100], )
    #pygame.draw.arc(screen, BLACK, [20,20,250,100],  PI/2,     PI, 20)
    
    pygame.draw.polygon(screen, BLACK, [[353,20], [50,150], [650,150]], 0)

    # Select the font to use, size, bold, italics
    #font = pygame.font.SysFont('Calibri', 25, True, False)
     
    # Render the text. "True" means anti-aliased text.
    # Black is the color. The variable BLACK was defined
    # above as a list of [0, 0, 0]
    # Note: This line creates an image of the letters,
    # but does not put it on the screen yet.
    #text = font.render("Henry's Game",True,BLACK)
     
    # Put the image of the text on the screen at 250x250
    #screen.blit(text, [100, 300])    
    
    #for x_offset in range(0, 100, 10):
        #pygame.draw.line(screen, GREEN, [20, 20], [100, 20], 5)
        #pygame.draw.line(screen, GREEN, [100, 20], [100, 150], 5)
        #pygame.draw.line(screen, GREEN, [100, 150], [20, 150], 5)
        #pygame.draw.line(screen, GREEN, [20, 150], [20, 20], 5)  
        
        
    
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    
            
pygame.quit()