import pygame, sys, random, time
from pygame.locals import *

# Инициализация Pygame и звукового движка
pygame.init()
pygame.mixer.init()

# Фоновая музыка
pygame.mixer.music.load(r"C:\Users\HOME\Desktop\pp2_2025\lab8\racer\background.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)  # -1 означает бесконечный повтор

# Цвета (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)

# Размеры экрана
w, h = 400, 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("RACE GAME")

# Фон игры
background = pygame.image.load(r"C:\Users\HOME\Desktop\pp2_2025\lab8\racer\AnimatedStreet.png")

# Переменные игры
FPS = 60
clock = pygame.time.Clock()
speed = 5
score = 0
coins_collected = 0
coins_needed_for_speedup = 5
sc = 0  # Для отслеживания увеличения скорости

# --- Классы ---

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\HOME\Desktop\pp2_2025\lab8\racer\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w - 40), 0)

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.bottom > h:
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
        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] and self.rect.right < w:
            self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self, image_path, value):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w - 40), random.randint(50, h - 200))
        self.value = value  # Вес монеты (1, 2 или 3)

    def move(self):
        self.rect.move_ip(0, 3)  # Плавное падение
        if self.rect.top > h:
            self.respawn()

    def respawn(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, w - 40), random.randint(50, h - 200))

    def collect(self):
        pygame.mixer.Sound(r"C:\Users\HOME\Desktop\pp2_2025\lab8\racer\coin.mp3").play()
        self.respawn()

# --- Создание объектов ---

P1 = Player()
E1 = Enemy()

# Создаём монеты с разными весами
coins = pygame.sprite.Group()
coin_types = [
    (r"C:\Users\HOME\Desktop\pp2_2025\lab8\racer\coin.jpg", 1),  # Обычная монета
    (r"C:\Users\HOME\Desktop\pp2_2025\lab8\racer\coin1.png", 2)  # Редкая монета
]

for img, value in coin_types:
    for _ in range(2):  # По 2 монеты каждого типа
        coin = Coin(img, value)
        coins.add(coin)

# Группы спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, *coins)

# Событие для увеличения скорости
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Шрифты
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# --- Игровой цикл ---
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            speed += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    scores = font_small.render(f"Score: {score}  Coins: {coins_collected}", True, BLACK)
    screen.blit(scores, (10, 10))

    # Двигаем и рисуем все объекты
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    # Проверяем столкновение игрока с монетами
    collected_coins = pygame.sprite.spritecollide(P1, coins, False)
    for coin in collected_coins:
        coins_collected += coin.value
        score += coin.value
        coin.collect()  # Монета исчезает и появляется заново

    # Увеличиваем скорость при достижении N монет
    if coins_collected >= coins_needed_for_speedup:
        speed += 1
        coins_collected = 0

    # Проверяем столкновение с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound(r"C:\Users\HOME\Desktop\pp2_2025\lab8\racer\crash.wav").play()
        time.sleep(1)

        screen.fill(RED)
        screen.blit(game_over, (30, 250))
        pygame.display.update()

        # Удаляем все спрайты и завершаем игру
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(FPS)