from pprint import pprint
from collections import deque
import copy
import grid_helper as gh


def scan_grid(grid, start=(0, 0)):
    """Scan all grid, so we can find a path from 'start' to any point"""

    q = deque()
    q.append(start)
    came_from = {start: None}
    while len(q) > 0:
        current_pos = q.popleft()
        neighbors = gh.get_neighbors(grid, current_pos[0], current_pos[1])
        for neighbor in neighbors:
            if neighbor not in came_from:
                q.append(neighbor)
                came_from[neighbor] = current_pos

    return came_from


def init():
    initial_grid = gh.generate_grid_obstacle_for_b_star()
    start_pos = (3, 0)
    directions = scan_grid(initial_grid, start_pos)

    path1 = gh.find_path(start_pos, (8, 8), directions)
    # need copy as we modify the grid
    grid_with_path1 = gh.draw_path(path1, copy.deepcopy(initial_grid))
    pprint(grid_with_path1)
    print(f"steps: {len(path1)}")

    path2 = gh.find_path(start_pos, (4, 7), directions)
    grid_with_path2 = gh.draw_path(path2, copy.deepcopy(initial_grid))
    pprint(grid_with_path2)
    print(f"steps: {len(path2)}")


if __name__ == "__main__":
    init()

