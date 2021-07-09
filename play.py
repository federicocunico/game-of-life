import pygame
import sys

from src.game_structures import GameState
from src.game_logic import GameLogic

pygame.init()
pygame.font.init()
font_size = 30
# text_font = pygame.font.SysFont('Comic Sans MS', font_size)

size = width, height = 800, 800

black = 50, 50, 50
gray = 125, 125, 125
white = 255, 255, 255
border_color = 55, 136, 216

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

speed = 60  # FPS

# Grid params
base_offset = 15
grid_rect_size = 10


def start_game_loop():
    while True:
        # delta_time = clock.get_time()

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_DOWN:
                    pass
                if event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_LEFT:
                    pass

                if event.key == pygame.K_r:
                    g.reset(is_init=True)

                if event.key == pygame.K_q:
                    # pygame.display.quit()
                    pygame.quit()
                    sys.exit()

        # rendering
        screen.fill(black)
        # print_grid()
        render_game()

        g.update()

        pygame.display.flip()
        clock.tick(speed)


def render_game():
    # borders
    pygame.draw.rect(
        screen,
        border_color,
        [
            base_offset,
            base_offset,
            GameState.game_width * grid_rect_size,
            GameState.game_height * grid_rect_size
        ],
        3
    )

    # all cells
    # for tup in GameState.changed_cells:
    #     i, j, val = tup
    #     color = black if not val else white  # white cells are live    
    #     pygame.draw.rect(
    #             screen,
    #             color,
    #             [
    #                 base_offset + i * grid_rect_size,
    #                 base_offset + j * grid_rect_size,
    #                 grid_rect_size,
    #                 grid_rect_size
    #             ]
    #         )

    cells = GameState.cells
    for i in range(cells.shape[0]):
        for j in range(cells.shape[1]):
            b = cells[i, j]
            color = black if not b else white  # white cells are live
            pygame.draw.rect(
                screen,
                color,
                [
                    base_offset + i * grid_rect_size,
                    base_offset + j * grid_rect_size,
                    grid_rect_size,
                    grid_rect_size
                ]
            )


def print_grid():
    for i in range(GameState.game_width):
        for j in range(GameState.game_height):
            pygame.draw.rect(
                screen,
                gray,
                [
                    (i * grid_rect_size) + base_offset,
                    (j * grid_rect_size) + base_offset,
                    grid_rect_size,
                    grid_rect_size
                ],
                1
            )


if __name__ == "__main__":
    g = GameLogic()
    g.start()
    start_game_loop()
