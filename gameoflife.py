import pygame
import random


WINDOW_HEIGHT, WINDOW_WIDTH = 1000, 1000
TILE_SIZE = 20
BACKGROUND_COLOR = (36, 40, 36)
FOREGROUND_COLOR = (232, 213, 176)

pulsar_board = [[0 for _ in range(WINDOW_HEIGHT // TILE_SIZE)] for _ in range(WINDOW_WIDTH // TILE_SIZE)]

pulsar = [
    (21, 18), (22, 18), (23, 18), (27, 18), (28, 18), (29, 18),
    (18, 21), (23, 21), (25, 21), (30, 21),
    (18, 22), (23, 22), (25, 22), (30, 22),
    (18, 23), (23, 23), (25, 23), (30, 23),
    (21, 25), (22, 25), (23, 25), (27, 25), (28, 25), (29, 25),
    (21, 27), (22, 27), (23, 27), (27, 27), (28, 27), (29, 27),
    (18, 30), (23, 30), (25, 30), (30, 30),
    (18, 31), (23, 31), (25, 31), (30, 31),
    (18, 32), (23, 32), (25, 32), (30, 32),
    (21, 33), (22, 33), (23, 33), (27, 33), (28, 33), (29, 33),
]
for cell in pulsar:
    pulsar_board[cell[1]][cell[0]] = 1


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


def get_neighbors(game_board: list[list[int]], row: int, col: int) -> list[int]:
    size = len(game_board)
    neighbors = []

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for row_move, col_move in directions:
        new_row, new_col = row + row_move, col + col_move
        if 0 <= new_row < size and 0 <= new_col < size:
            neighbors.append(game_board[new_row][new_col])

    return neighbors


def update_board(game_board: list[list[int]]) -> None:
    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            live_neighbors = get_neighbors(game_board, i, j).count(1)
            if live_neighbors < 2 and game_board[i][j]:
                game_board[i][j] = 0
            elif 2 <= live_neighbors <= 3 and game_board[i][j]:
                continue
            elif live_neighbors > 3 and game_board[i][j]:
                game_board[i][j] = 0
            elif live_neighbors == 3 and game_board[i][j] == 0:
                game_board[i][j] = 1


board = generate_random_board(0.07)
# board = pulsar_board


def toggle_cell(game_board, row, col):
    game_board[row][col] = 1 if game_board[row][col] == 0 else 0


def draw_cells(game_screen, game_board):
    size = WINDOW_WIDTH // TILE_SIZE
    for i in range(size):
        for j in range(size):
            if game_board[i][j] == 1:
                pygame.draw.rect(game_screen, FOREGROUND_COLOR,
                                 pygame.Rect(i * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                )


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

    update_board(board)
    draw_cells(screen, board)

    pygame.display.flip()

    clock.tick(15)

pygame.quit()
