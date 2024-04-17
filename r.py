import pygame
pygame.init()

X = 560
Y = 370
scrn = pygame.display.set_mode((X, Y))
pygame.display.set_caption('image')
imp = pygame.image.load("./7.jpg").convert()
scrn.blit(imp, (0, 0))
pygame.display.flip()
status = True
while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
pygame.quit()