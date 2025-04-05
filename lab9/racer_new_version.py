import pygame, sys, random, time
from pygame.locals import *

# Initialize Pygame and sound engine
pygame.init()
pygame.mixer.init()

# Background music
pygame.mixer.music.load(r"C:\Users\HOME\Desktop\pp2_2025\lab8\racer\background.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)  # -1 means infinite loop

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)

# Screen size
w, h = 400, 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("RACE GAME")

# Game background
background = pygame.image.load(r"C:\Users\HOME\Desktop\pp2_2025\lab8\racer\AnimatedStreet.png")

# Game variables
FPS = 60
clock = pygame.time.Clock()
speed = 5
score = 0
coins_collected = 0
coins_needed_for_speedup = 5
sc = 0  # For tracking speed increase

time = 10
sec = 1
# --- Classes ---

class Enemy(pygame.sprite.Sprite):  # Enemy car class
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

class Player(pygame.sprite.Sprite):  # Player car class
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

class Coin(pygame.sprite.Sprite):  # Coin class
    def __init__(self, image_path, value):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w - 40), random.randint(50, h - 200))
        self.value = value  # Coin value (1, 2 or 3)

    def move(self):
        self.rect.move_ip(0, 3)  # Smooth falling
        if self.rect.top > h:
            self.respawn()  # If it goes out of screen, respawn it above

    def respawn(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, w - 40), random.randint(50, h - 200))

    def collect(self):
        pygame.mixer.Sound(r"C:\Users\HOME\Desktop\pp2_2025\lab8\racer\coin.mp3").play()
        self.respawn()

# --- Create objects ---

P1 = Player()
E1 = Enemy()

# Create coins with different values
coin_types = [
    (r"C:\Users\HOME\Desktop\pp2_2025\lab8\racer\coin.jpg", 1),  # Normal coin
    (r"C:\Users\HOME\Desktop\pp2_2025\lab8\racer\coin1.png", 2)  # Rare coin
]

coins = pygame.sprite.Group()
for img, value in coin_types:
    for _ in range(2):  # 2 coins of each type
        coin = Coin(img, value)
        coins.add(coin)

# Sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, *coins)

# Event for increasing speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# --- Game loop ---
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            speed += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    scores = font_small.render(f"Score: {score}  Coins: {coins_collected} Timer:{time}", True, BLACK)
    screen.blit(scores, (10, 10))

    # Move and draw all objects
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    # Check player collision with coins
    collected_coins = pygame.sprite.spritecollide(P1, coins, False)
    for coin in collected_coins:
        coins_collected += coin.value
        score += coin.value
        coin.collect()  # Coin disappears and respawns

    # Increase speed after collecting N coins
    if coins_collected >= coins_needed_for_speedup:
        speed += 1
        coins_collected = 0

    # Check collision with enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound(r"C:\Users\HOME\Desktop\pp2_2025\lab8\racer\crash.wav").play()
        time.sleep(1)

        screen.fill(RED)
        screen.blit(game_over, (30, 250))
        pygame.display.update()

        # Delete all sprites and quit game
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
        
        

    pygame.display.update()
    clock.tick(FPS)