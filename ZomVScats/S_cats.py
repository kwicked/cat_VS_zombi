from random import choice, randint
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
    def __init__(self, player_image, player_x, player_y, player_speed,size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Bullet(GameSprite):
    def update(self): 
        self.rect.x -= self.speed
        if  self.rect.x <= 0:
            self.kill()
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self. rect.y < 400:
            self.rect.y += self.speed 
    def fire(self):
        fruct = Bullet('aplle.png',self.rect.centerx,self.rect.top, -10, 55, 50)
        fructs.add(fruct)
class Zombi(GameSprite):
    def update(self):
        self.rect.x -= self.speed
        global lost
        if self.rect.x == 0:
            self.rect.x = 690
            self.rect.y = randint(80, 620)
            lost = lost + 1
cat = Player('cat1.png', 30, 200, 10, 100, 100)
lost = 0
score = 0
fructs = sprite.Group()
zombis = sprite.Group()
spisok_mosrtr= ['zombi1.png','zombi2.png','zombi3.png']
for i in range(6):
    zombi = Zombi(choice(spisok_mosrtr),690,randint(80, 400), randint(1,5),100,100) 
    zombis.add(zombi)
finish = False
num_fire = 0
rel_time = False
score = 0
font.init()
font1 = font.SysFont('Arial',35)
font2 = font.SysFont('Arial',100)
win = font2.render('You Win!', True, (19, 58, 15))
lose = font2.render('You Lose.', True, (180, 0,  0))
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
        zombis.update()
        zombis.draw(window)
        cat.reset()
        cat.update()
        fructs.update()
        fructs.draw(window)

        sprites_list = sprite.groupcollide(fructs, zombis, True, True)
        for vrag in sprites_list:
            score = score+1
            zombi = Zombi(choice(spisok_mosrtr),690,randint(80, 400), randint(1,5),100,100) 
            zombis.add(zombi)
        if score >= 10:
            finish = True
            window.blit(win,(210,200))
        if lost >= 13 or sprite.spritecollide(cat, zombis, False):
            finish = True
            window.blit(lose,(250,250))
        text_lose = font1.render('Пропущено: ' + str(lost), 1, (212, 48, 35))
        text_win = font1.render('Счет: ' + str(score), 1, (212, 48, 35))
        window.blit(text_win,(5, 10))
        window.blit(text_lose,(5, 50))

        display.update()
        time.delay(30)
