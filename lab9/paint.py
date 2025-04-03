import pygame

white = (255, 255, 255)
eraser = (0, 0, 0)
green = (34, 139, 34)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
pygame.display.set_caption("Paint")

def main():
    radius = 2
    mode = white
    last_pos = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    return
                
                if event.key == pygame.K_r:
                    mode = red
                elif event.key == pygame.K_y:
                    mode = yellow
                elif event.key == pygame.K_b:
                    mode = blue
                elif event.key == pygame.K_w:
                    mode = white
                elif event.key == pygame.K_g:
                    mode = green
                elif event.key == pygame.K_r:
            
            
