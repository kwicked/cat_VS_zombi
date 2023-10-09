#Создай собственный Шутер!
from random import randint
from pygame import *
from time import time as timer
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Shooter Game")
background = transform.scale(image.load("galaxy.jpg"),(win_width, win_height))
FPS = 360
clock = time.Clock()
run = True
finish = False
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
kick = mixer .Sound('fire.ogg')
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
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self. rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png',self.rect.centerx,self.rect.top, -10, 10, 30)
        bullets.add(bullet)
lost = 0
score = 0

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= win_height:
            self.rect.y = 0
            self.rect.x = randint(80, 620)
            lost = lost + 1
class Enemy2(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= win_height:
            self.rect.y = 0
            self.rect.x = randint(80, 620)
        
class Bullet(GameSprite):
    def update(self): 
        self.rect.y += self.speed
        if  self.rect.y <= 0:
            self.kill()
player = Player("rocket.png", 310, 400, 4, 65, 65)
monsters = sprite.Group()
asteroids = sprite.Group()
for i in range(5):
    monster = Enemy('ufo.png', randint(80, 620), 0, randint(1,2), 90, 65)
    monsters.add(monster)
    asteroid = Enemy2('asteroid.png', randint(80, 620), 0, randint(1,2), 90, 65)
    asteroids.add(asteroid)
font.init()
font1 = font.SysFont('Arial',35)
font2 = font.SysFont('Arial',80)
win = font2.render('You Win!', True, (255, 255, 255))
lose = font2.render('You Lose.', True, (180, 0,  0))
health = 3
bullets = sprite.Group()
rel_time = False
num_fire = 0
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire < 5 and rel_time == False:
                    num_fire = num_fire +1
                    kick.play()
                    player.fire()
                if num_fire >= 5 and rel_time == False:
                    last_time = timer()
                    rel_time = True
    if finish != True:
        window.blit(background, (0,0))
        player.update()
        player.reset()
        monsters.update()
        monsters.draw(window)
        asteroids.update()
        asteroids.draw(window)
        bullets.update()
        bullets.draw(window)
        sprites_list = sprite.groupcollide(bullets, monsters, True, True)
        if rel_time == True:
            now_time = timer()
            if now_time - last_time < 3:
                reload = font2.render('Перезарядка.....', 1, (150,0,0))
                window.blit(reload, (260, 460))
            else:
                num_fire = 0
                rel_time = False
        for vrag in sprites_list:
            score = score+1
            monster = Enemy('ufo.png', randint(80, 620), 0, randint(1,2), 90, 65)
            monsters.add(monster)
        if score >= 10:
            finish = True
            window.blit(win,(250,250))
        if lost >= 3 or sprite.spritecollide(player, monsters, False):
            finish = True
            window.blit(lose,(250,250))
        if sprite.spritecollide(player, asteroids, False):
            health-=1
            sprite.spritecollide(player, asteroids, True)
        if health ==0:
            finish = True
            window.blit(lose,(250,250))
        text_lose = font1.render('Пропущено:' + str(lost), 1, (255, 255, 255))
        text_win = font1.render('Счет:' + str(score), 1, (255, 255, 255))
        window.blit(text_lose,(5, 10))
        window.blit(text_win,(5, 40))
        text_health = font2.render(str(health), 1, (155, 255, 255))
        window.blit(text_health,(650, 10))
        display.update()
        clock.tick(FPS)