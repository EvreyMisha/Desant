import pygame
import random
clock = pygame.time.Clock()

pygame.init()
height = 300
width = 794
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Крес")

all_sprites = pygame.sprite.Group()
mountain = pygame.sprite.Group()
pt = pygame.sprite.Group()


class Mountain(pygame.sprite.Sprite):
    image = pygame.image.load("data/mountains.png")

    def __init__(self):
        super().__init__(mountain)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.add(mountain)
        self.rect.bottom = height

class Landing(pygame.sprite.Sprite):
    image = pygame.image.load("data/pt.png")

    def __init__(self, pos):
        super().__init__(pt)
        self.image = Landing.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.add(pt)

    def update(self):
        if not pygame.sprite.collide_mask(self, mount):
            self.rect = self.rect.move(0, 1)

mount = Mountain()

run = True
while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False
        if eve.type == pygame.MOUSEBUTTONDOWN:
            Landing(eve.pos)
    win.fill((0, 0, 0))
    pt.update()
    mountain.draw(win)
    pt.draw(win)
    clock.tick(10)
    pygame.display.flip()

pygame.quit()