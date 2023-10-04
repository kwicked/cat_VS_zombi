from random import randint
from pygame import *

win_width = 700
win_height = 500

FPS = 60

clock = time.Clock()
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong!')
background = transform.scale(image.load('cool_cat.jpg'),(win_width, win_height))
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

ball = GameSprite('ball pp.png', 280,200, 10,75,75)   
pl1 = Player('finish.png', 0, 300, 10,30,150)
pl2 = Player('finish.png', 670, 300, 10,30,150)
finish = False

speed_x = 3
speed_y = 3

font.init()
font1 = font.Font(None, 50)
lose1 = font1.render('ИГРОК 1 ПРОИГРАЛ', True, (180, 200, 0))
lose2 = font1.render('ИГРОК 2 ПРОИГРАЛ', True, (180, 200, 0))

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    

        
    window.blit(background, (0,0))
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(pl1, ball) or sprite.collide_rect(pl2, ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
    if ball.rect.x > win_width-80:
        finish = True
        window.blit(lose2, (200, 200))
    ball.reset()
    pl1.update_l()
    pl1.reset()
    pl2.update_r()
    pl2.reset()
    display.update()
    time.delay(30)