import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')


class Soldier(pygame.sprite.Sprite):
    def __init__(self,x,y,scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("img/player/Idle/0.png")
        self.img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale) ))
        self.rect = self.img.get_rect()
        self.rect.center = (x,y)


player = Soldier(200, 200, 3)        



run = True

while run:

    screen.blit(player.img, player.rect)


    for event in pygame.event.get():
        #quitgame
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()        

pygame.quit()            