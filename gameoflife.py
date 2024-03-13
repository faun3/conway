import pygame
import random


WINDOW_HEIGHT, WINDOW_WIDTH = 1000, 1000
TILE_SIZE = 20
BACKGROUND_COLOR = (36, 40, 36)
FOREGROUND_COLOR = (232, 213, 176)


def generate_random_board(live_density: float) -> list[list[int]]:
    size = WINDOW_WIDTH // TILE_SIZE
    generated_board = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if random.random() < live_density:
                generated_board[i][j] = 1
            else:
                generated_board[i][j] = 0

    return generated_board


board = generate_random_board(0.15)


def toggle_cell(game_board, row, col):
    game_board[row][col] = 1 if game_board[row][col] == 0 else 0


def draw_cells(game_screen, game_board):
    size = WINDOW_WIDTH // TILE_SIZE
    for i in range(size):
        for j in range(size):
            if game_board[i][j] == 1:
                pygame.draw.rect(game_screen, FOREGROUND_COLOR, pygame.Rect(i * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE))


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

    draw_cells(screen, board)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
