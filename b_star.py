"""
Best First Search (greedy algorithm),
always move to the end point, not good with obstacles, can find not the shortest path
"""

from queue import PriorityQueue
import grid_helper as gh
from pprint import pprint


def find_path_greedy(grid, start, end):
    pq = PriorityQueue()
    pq.put((0, start))
    came_from = {start: None}

    while not pq.empty():
        current_pos = pq.get()[1]

        if current_pos == end:
            break

        neighbors = gh.get_neighbors(grid, current_pos[0], current_pos[1])
        for neighbor in neighbors:
            if neighbor not in came_from:
                priority = gh.heuristic_distance(neighbor, end, type="e")
                grid[neighbor[0]][neighbor[1]] = "x"
                pq.put((priority, neighbor))
                came_from[neighbor] = current_pos

    return came_from


def init():
    initial_grid = gh.generate_grid_empty()
    start, end = (1, 0), (8, 8)
    came_from = find_path_greedy(initial_grid, start, end)
    path = gh.find_path(start, end, came_from)
    gh.draw_path(path, initial_grid)

    pprint(initial_grid)


if __name__ == "__main__":
    init()
