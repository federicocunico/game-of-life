import time
import numpy as np
from threading import Thread

from src.game_structures import GameState as g


adjust_speed = False


class GameLogic(Thread):
    def __init__(self):
        super().__init__()

        self._stop = False

    min_interval = 0.03
    max_interval = 0.2  # 0.2

    def stop(self):
        self._stop = True

    def init_game(self):
        self.reset(is_init=True)

    def run(self):
        self.init_game()

        while not self._stop:

            self.update()

            # Adjust speed
            if adjust_speed:
                interval = self.max_interval - g.game_speed * 0.01
                if interval < self.min_interval:
                    interval = self.min_interval
            else:
                interval = self.max_interval

            time.sleep(interval)

        print('Finished')

    @staticmethod
    def update():
        # to update logic
        """

        1. Any live cell with two or three live neighbours survives.
        2. Any dead cell with three live neighbours becomes a live cell.
        3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.
        """

        # g.changed_cells.clear()

        start = time.time()
        cells = g.cells
        w, h = cells.shape[0:2]
        copy = np.array(cells)

        def get_live_state(pos_x, pos_y) -> bool:
            if pos_x >= w or pos_y >= h:
                return False
            elif pos_x < 0 or pos_y < 0:
                return False
            else:
                return copy[pos_x, pos_y]
        # return
        for i in range(w):
            for j in range(h):
                curr_live_state = copy[i, j]

                # go watch 8 neigh
                upleft_x = i-1
                upleft_y = j-1
                upleft_live_state = get_live_state(upleft_x, upleft_y)

                up_x = i-1
                up_y = j
                up_live_state = get_live_state(up_x, up_y)

                upright_x = i-1
                upright_y = j+1
                upright_live_state = get_live_state(upright_x, upright_y)

                right_x = i
                right_y = j+1
                right_live_state = get_live_state(right_x, right_y)

                downright_x = i+1
                downright_y = j+1
                downright_live_state = get_live_state(downright_x, downright_y)

                down_x = i+1
                down_y = j
                down_live_state = get_live_state(down_x, down_y)

                downleft_x = i+1
                downleft_y = j-1
                downleft_live_state = get_live_state(downleft_x, downleft_y)

                left_x = i
                left_y = j-1
                left_live_state = get_live_state(left_x, left_y)

                states = [
                    upleft_live_state,
                    up_live_state,
                    upright_live_state,
                    right_live_state,
                    downright_live_state,
                    down_live_state,
                    downleft_live_state,
                    left_live_state
                ]

                num_neigh_live = sum([1 if s else 0 for s in states])

                # if num_neigh_live > 0:
                # print('X', i, 'Y', j, '#live neigh', num_neigh_live, 'state', curr_live_state)

                # 1. Any live cell with two or three live neighbours survives.
                if curr_live_state and (num_neigh_live == 2 or num_neigh_live == 3):
                    to_set_value = True

                # 2. Any dead cell with three live neighbours becomes a live cell.
                elif (not curr_live_state) and (num_neigh_live == 3):
                    to_set_value = True

                # 3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.
                else:
                    to_set_value = False

                cells[i, j] = to_set_value
                # g.changed_cells.append((i, j, to_set_value))

            for tup in g.changed_cells:
                i, j, val = tup
                cells[i, j] = val

        print(f'Loop in {time.time() - start}')

    def reset(self, is_init=False):
        g.reset(is_init)
