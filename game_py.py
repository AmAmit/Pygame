import pygame
import random
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GOLD = (255,215,0)
x= 0
y= 215
x_speed=0
y_speed=0
background_position = [0, 0]

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("alie.gif").convert()
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x-=2
 
class Player(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("spaceship.gif").convert()
        self.rect = self.image.get_rect()
 
    def update(self):
        self.rect.x = x
        self.rect.y = y
  
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 4])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
 
    def update(self):
        self.rect.x += 3
 
pygame.init()
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("LOl maxxx")
background_image = pygame.image.load("space.jpg").convert() 
click_sound = pygame.mixer.Sound("laser5.ogg")
all_sprites_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
 
for i in range(300):
    block = Block()
    block.rect.x = random.randrange(210,16000)
    block.rect.y = random.randrange(600)
    block_list.add(block)
    all_sprites_list.add(block)
    
player = Player()
all_sprites_list.add(player)

done = False
clock = pygame.time.Clock()
score = 0
game_over=False
font= pygame.font.Font(None,36)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
            bullet = Bullet()
            bullet.rect.x = x+183
            bullet.rect.y = y+39
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -5
            elif event.key == pygame.K_RIGHT:
                x_speed = 5
            elif event.key == pygame.K_UP:
                y_speed = -5
            elif event.key == pygame.K_DOWN:
                y_speed = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
    x = x + x_speed
    y = y + y_speed
    if x<=0:
        x=0
    elif x>=625:
        x=625
    if y<=-25:
        y=-25
    elif y>450:
        y=450

    all_sprites_list.update()
 
    for bullet in bullet_list:
 
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
 
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 5
            print(score)
 
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
    for block in block_list:
        if pygame.sprite.collide_rect(player,block):
            done=True

    screen.blit(background_image, background_position)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()
