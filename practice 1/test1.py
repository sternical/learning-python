
import pygame 
  
pygame.init() 
  
color = (255,255,255) 
Background_color = (160,32,240) 
  
# Take image as input 
img = pygame.image.load('Capture.PNG') 
  
# Set image as icon 
pygame.display.set_icon(img) 

# CREATING CANVAS 
canvas = pygame.display.set_mode((400, 400),pygame.RESIZABLE) 
  
# CANVAS COLOR
canvas.fill(Background_color)
pygame.display.flip()

# TITLE OF CANVAS 
pygame.display.set_caption("Practice game") 

# creating a bool value which checks 
# if game is running
running = True
 
# Game loop
# keep game running till running is true
while running:
   
    # Check for event if user has pushed 
    # any event in queue
    for event in pygame.event.get():
       
        # if event is of type quit then set
        # running bool to false
        if event.type == pygame.QUIT:
            running = False
            