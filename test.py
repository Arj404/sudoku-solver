import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Test Game")

x=0
y=0
width = 40
height = 60
vel=5

run=True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x = (x-vel)%500
    if keys[pygame.K_RIGHT]:
        x = (x+vel)%500
    if keys[pygame.K_UP]:
        y = (y-vel)%500
    if keys[pygame.K_DOWN]:
        y = (y+vel)%500
    
    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x,y,width,height))
    pygame.display.update()

pygame.quit()