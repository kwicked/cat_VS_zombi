from random import randint
from pygame import *

win_width = 700
win_height = 500

FPS = 60

clock = time.Clock()
window = display.set_mode((win_width, win_height))
display.set_caption('Zombi V/S Cats')
background = transform.scale(image.load('u.jpg'),(win_width, win_height))
run = True

class GameSprite(sprite.Sprite):
    def __init__(self, pl_image, pl_x, pl_y, pl_sped,size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(pl_image), (size_x, size_y))
        self.speed = pl_sped
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

zombi = GameSprite('zombi1.png', 280,200, 10,75,75) 

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background, (0,0))
    display.update()
    time.delay(30)
