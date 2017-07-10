"""
Dijkstra algorithm, find the cheapest path.
if price is the same for every move it works like BFS
"""

from queue import PriorityQueue
import grid_helper as gh
from pprint import pprint


def find_path_a_star(grid, start, end):
    pq = PriorityQueue()
    pq.put((0, start))
    came_from = {start: None}
    costs = {start: 0}

    while not pq.empty():
        current_pos = pq.get()[1]

        if current_pos == end:
            break

        neighbors = gh.get_neighbors(grid, current_pos[0], current_pos[1])

        for neighbor in neighbors:
            new_cost = costs[current_pos] + gh.get_cost(grid, neighbor)

            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                priority = new_cost + gh.heuristic_distance(neighbor, end)
                pq.put((priority, neighbor))
                came_from[neighbor] = current_pos

    return came_from


def init():
    initial_grid = gh.generate_grid_weighted()
    start, end = (4, 0), (4, 6)
    came_from = find_path_a_star(initial_grid, start, end)
    path = gh.find_path(start, end, came_from)
    gh.draw_path(path, initial_grid)

    pprint(initial_grid)


if __name__ == "__main__":
    init()
