import pygame , sys
from pygame.locals import*
import random, time

#to initialize the library
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load(r"C:\Users\HOME\Desktop\pp2_2025\lab8\racer\background.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)  # -1 означает, что музыка будет играть бесконечно

#Colors in format (R, G, B) 
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

w = 400
h = 600

screen = pygame.display.set_mode((w,h))
screen.fill(WHITE)
pygame.display.set_caption("RACE GAME")
background = pygame.image.load(r"C:\Users\HOME\Desktop\pp2_2025\lab8\racer\AnimatedStreet.png")

FPS = 60
clock = pygame.time.Clock()

speed = 5
score = 0
coins_collected = 0
coins_needed_for_speedup = 5
sc = 0

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\HOME\Desktop\pp2_2025\lab8\racer\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w - 40), 0)

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if (self.rect.bottom > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, w - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\HOME\Desktop\pp2_2025\lab8\racer\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < w:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\HOME\Desktop\pp2_2025\lab8\racer\coin.jpg")  # Загрузи картинку монеты
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w - 40), random.randint(50, h - 200))

        # Разные веса монет
        self.value = random.choice([1, 2, 3])  # 1 - бронзовая, 2 - серебряная, 3 - золотая
    
    def move(self):
        self.rect.move_ip(0, 3)  # Медленное падение монеты
        if self.rect.top > h:
            self.rect.top = 0
            self.rect.center = (random.randint(40, w - 40), random.randint(50, h - 200))
    
    def disappear(self):
        self.rect.top = 0
        pygame.mixer.Sound(r"C:\Users\HOME\Desktop\pp2_2025\lab8\racer\coin.mp3").play()
        self.rect.center = (random.randint(40, w - 40), 0)

class Coin2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\HOME\Desktop\pp2_2025\lab8\racer\coin1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, 1)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, w - 40), 0)

    def disappear(self):
        self.rect.top = 0
        pygame.mixer.Sound(r"C:\Users\HOME\Desktop\pp2_2025\lab8\racer\coin.mp3").play()
        self.rect.center = (random.randint(40, w - 40), 0)

P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()  # Группа монет
for _ in range(3):  # Создаём 3 монеты
    coin = Coin()
    coins.add(coin)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(*coins)

# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()
C2 = Coin2()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
coins1 = pygame.sprite.Group()
coins1.add(C2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(C2)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)


while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              speed += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0,0))
    scores = font_small.render(str(score), True, BLACK)
    screen.blit(scores, (10,10))

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(P1, coins):
        Coin.disappear(C1)
        score += 1
    if score // 2>>sc:
        speed += 1
        sc += 1
        
    if pygame.sprite.spritecollideany(P1, coins1):
        Coin.disappear(C2)
        score += 2
    if score // 2>>sc:
        speed += 1
        sc += 1
    

    font = pygame.font.SysFont('Bauhaus 93', 20)
    text = font.render('Speed: ' + str(speed - 5), True, BLACK)
    screen.blit(text, (w - 140, 10))

    # Проверка на столкновение с монетами
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collected_coins:
        coins_collected += coin.value  # Увеличиваем количество монет по весу
        new_coin = Coin()  # Создаём новую монету после сбора
        coins.add(new_coin)
        all_sprites.add(new_coin)

    # Увеличиваем скорость врага при достижении N монет
    if coins_collected >= coins_needed_for_speedup:
        speed += 1  # Увеличиваем скорость
        coins_collected = 0  # Обнуляем счётчик монет для следующего прироста скорос

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound(r"C:\Users\HOME\Desktop\pp2_2025\lab8\racer\crash.wav").play()
        time.sleep(1)
        
        screen.fill(RED)
        screen.blit(game_over, (30,250))
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()  

    pygame.display.update()
    clock.tick(FPS)