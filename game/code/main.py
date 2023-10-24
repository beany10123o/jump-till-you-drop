import sys, pygame, os, random #Import all needed modules

#This is the "game" folder to get files from
working_path = os.path.dirname(os.path.join(os.path.dirname(__file__), "..", ".."))

#Set window details
window_name = 'hello'
window_size = (500, 500) #width, height
background_colour = (0, 0, 255)

#Setup sprites
draa_standing = pygame.image.load(os.path.join(working_path, "images", "sprites", "Draa", "standing.png"))
draa_jumping = pygame.image.load(os.path.join(working_path, "images", "sprites", "Draa", "jumping.png"))

#Initialise Window
screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)
pygame.display.set_caption(window_name)

position = [0, 40]
speed = [200, 0]

clock = pygame.time.Clock()
screen.fill((255, 255, 255))

#Game loop
while True:
    #Make the close button work
    #This also stops the program from making the cursor go into laggy mode
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    clock.tick()
    
    if(position[0] < 0):
        speed[0] = 200
        background_colour = (random.random() * 255, random.random() * 255, random.random() * 255)
    if(position[1] < 0):
        speed[1] = 220
        background_colour = (random.random() * 255, random.random() * 255, random.random() * 255)
    if(position[0] > screen.get_width() - 100):
        speed[0] = -200
        background_colour = (random.random() * 255, random.random() * 255, random.random() * 255)
    if(position[1] > screen.get_height() - 100):
        speed[1] = -abs(speed[1])
        background_colour = (random.random() * 255, random.random() * 255, random.random() * 255)
    speed[1] += 100 * clock.get_time() / 1000
    for i in range(2):
        position[i] += speed[i] * clock.get_time() / 1000

    #Draw the background
    screen.fill(background_colour)

    #Draw Draa
    if(speed[1] > 0):
        screen.blit(pygame.transform.smoothscale(draa_standing, (100, 100)), position)
    else:
        screen.blit(pygame.transform.smoothscale(draa_jumping, (100, 100)), position)

    #Put everything we have draw actually on the screen
    pygame.display.flip()