import pygame


WINDOW_HEIGHT, WINDOW_WIDTH = 1000, 1000
TILE_SIZE = 20
BACKGROUND_COLOR = (36, 40, 36)
FOREGROUND_COLOR = (232, 213, 176)


def draw_cell(screen, row, col):
    pygame.draw.rect(screen, FOREGROUND_COLOR, pygame.Rect(row * TILE_SIZE, col * TILE_SIZE, TILE_SIZE, TILE_SIZE))


pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("game of life")
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    draw_cell(screen, 1, 4)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
