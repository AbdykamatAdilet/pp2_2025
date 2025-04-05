import pygame
from random import randrange
from random import choice #to select random food we need to enable choice

pygame.init()

r = 600
size = 25
speed = 3
length = 1
x = randrange(0, r, size)
y = randrange(0, r, size)
snake = [(x, y)]
dx, dy = 0, 0
score = 0

#foods
foods = [
    {"color": "red", "points": 1, "size": size, "lifetime": 300},  
    {"color": "yellow", "points": 3, "size": size, "lifetime": 180},  
    {"color": "white", "points": 5, "size": size, "lifetime": 120} 
]

def new_food():
    food_type = choice(foods)  # Choose random food
    return {
        "pos": (randrange(0, r, size), randrange(0, r, size)),
        "color": food_type["color"],
        "points": food_type["points"],
        "size": food_type["size"],
        "lifetime": food_type["lifetime"]
    }

food = new_food()  #first food

apple = randrange(0, r, size), randrange(0, r, size)

FPS = 15

screen = pygame.display.set_mode((r, r))
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 50, bold=True)
pygame.display.set_caption("Snake game")

while True:
    screen.fill(pygame.Color(0, 0, 0))
    for i, j in snake:
        pygame.draw.rect(screen, pygame.Color('green'), (i, j, size, size))
    
    #Drawing apple
    pygame.draw.rect(screen, pygame.Color('red'), (*apple, size, size))

    #Drawing foods
    pygame.draw.rect(screen, pygame.Color(food["color"]), (*food["pos"], food["size"], food["size"]))

    #Display of points
    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    screen.blit(render_score, (5, 5))

    x += dx * size
    y += dy * size
    snake.append((x, y))
    snake = snake[-length:]

    #time of food
    food["lifetime"] -= 1
    if food["lifetime"] <= 0:
        food = new_food()  #If the timer runs out, create new food

    #Checking if the snake has eaten food
    if snake[-1] == food["pos"]:
        length += food["points"]  #Increase the length depending on the type of food
        score += food["points"]
        if FPS < 30:
            FPS += 0.5
        food = new_food()  #create a new food

    if snake[-1] == apple:
        apple = randrange(0, r, size), randrange(0, r, size)
        length += 2
        score += 1
        FPS += 0.5

    #If the snake collides with itself, the game is over
    if len(snake) != len(set(snake)):
        screen.fill(pygame.Color('black'))
        render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
        screen.blit(render_end, (r // 2 - 150, r // 3))
        pygame.display.flip()
        pygame.time.delay(2000)
        exit()

    #Walking through walls
    if x < 0:
        x = r - size  #If you go beyond the left border, we appear on the right
    elif x >= r:
        x = 0  #If you go beyond the right border, we appear on the left
    if y < 0:
        y = r - size  #If we go beyond the upper limit, we will end up at the bottom
    elif y >= r:
        y = 0  #If we go beyond the lower boundary, we appear at the top

    pygame.display.flip()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        dx, dy = 0, -1
    if key[pygame.K_DOWN]:
        dx, dy = 0, 1
    if key[pygame.K_LEFT]:
        dx, dy = -1, 0
    if key[pygame.K_RIGHT]:
        dx, dy = 1, 0