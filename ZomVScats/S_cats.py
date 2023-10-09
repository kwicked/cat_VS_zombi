from random import *
from pygame import *
from time import time as timer

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
    def update_ty(self):
        self.rect.x -= self.speed
        if self.rect.y <0:
            self.rect.x = 0
            self.rect.y = randint(80, 620)
class Bullet(GameSprite):
    def update(self): 
        self.rect.x -= self.speed
        if  self.rect.x <= 0:
            self.kill()
class Player(GameSprite):
    '''def update_l(self):
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
            self.rect.y += self.speed'''
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self. rect.y < win_width - 80:
            self.rect.y += self.speed 
    def fire(self):
        fruct = Bullet('aplle.png',self.rect.centerx,self.rect.top, -10, 55, 50)
        fructs.add(fruct)

cat = Player('cat1.png', 30, 200, 10, 100, 100) 
'''zombi = GameSprite('zombi1.png', 280,200, 10,75,75) 
zombi2 = GameSprite('zombi2.png', 280,200, 10,75,75)
zombi3 = GameSprite('zombi3.png', 280,200, 10,75,75)
'''
lost = 0
score = 0
fructs = sprite.Group()
zombis = sprite.Group()
for i in range(5):
    zombi = GameSprite('zombi1.png',650,randint(80, 400), randint(1,2),75,75) 
    zombi2 = GameSprite('zombi2.png', 450,randint(80, 400), 10,75,75)
    zombi3 = GameSprite('zombi3.png', 450,randint(80, 400), 10,75,75)
    zombis.add(zombi)
    'zombis.add(zombi2)'
finish = False
num_fire = 0
rel_time = False
score = 0

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                'if num_fire < 5 and rel_time == False:'
                num_fire = num_fire +1
                'kick.play()'
                cat.fire()
                '''if num_fire >= 5 and rel_time == False:
                    last_time = timer()
                    rel_time = True'''
    if finish != True:
        window.blit(background, (0,0))
        zombis.update_ty()
        cat.reset()
        cat.update()
        zombis.draw(window)
        fructs.update()
        fructs.draw(window)
        display.update()
        time.delay(30)