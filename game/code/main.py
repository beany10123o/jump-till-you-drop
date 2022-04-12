import sys, pygame, os #Import all needed modules

#This is the "game" folder to get files from
working_path = os.path.dirname(os.path.join(os.path.dirname(__file__), "..", ".."))

#Set window details
window_name = 'hello'
window_size = (500, 500) #width, height
background_colour = (0, 0, 255)

#Setup sprites
draa_jumping = pygame.image.load(os.path.join(working_path, "images", "sprites", "Draa", "jumping.png"))

#Initialise Window
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_name)

#Game loop
while True:
    #Make the close button work
    #This also stops the program from making the cursor go into laggy mode
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    #Draw the background
    screen.fill(background_colour)

    #Draw Draa
    screen.blit(draa_jumping, (0, 0))

    #Put everything we have draw actually on the screen
    pygame.display.flip()