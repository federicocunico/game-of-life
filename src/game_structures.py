import random
import numpy as np
from enum import IntEnum
from typing import List, Tuple


# class GridPosition:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def set_x(self, new_x):
#         self.x = new_x

#     def set_y(self, new_y):
#         self.y = new_y


# vGridPosition = np.vectorize(GridPosition)


class CellState(IntEnum):
    DEAD = 0
    LIVE = 1


class GameState:
    """

    1. Any live cell with two or three live neighbours survives.
    2. Any dead cell with three live neighbours becomes a live cell.
    3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.
    """
    game_width = 75
    game_height = 75
    game_speed = 1

    random_init = True
    initial_num_points = game_width * 600
    max_initial_num_points = int((game_width * game_height) * 7/8)

    cells: np.ndarray = np.zeros((game_width, game_height), dtype=bool)
    changed_cells = []

    @staticmethod
    def reset(is_init: bool):
        GameState.cells = np.zeros(
            (GameState.game_width, GameState.game_height), dtype=bool)

        if is_init:

            if GameState.random_init:
                num_pts = random.randint(0, GameState.max_initial_num_points)
            else:
                if GameState.initial_num_points > GameState.max_initial_num_points:
                    print(
                        f'Initial num points: {GameState.initial_num_points} exceeds max allowed num points for this grid: {GameState.max_initial_num_points} (grid: {GameState.game_width} by {GameState.game_height})')
                    num_pts = GameState.max_initial_num_points
                else:
                    num_pts = GameState.initial_num_points

            for _ in range(num_pts):
                x = random.randint(0, GameState.game_width-1)
                y = random.randint(0, GameState.game_height-1)
                GameState.cells[x, y] = True
                # GameState.changed_cells.append((x, y, True))
