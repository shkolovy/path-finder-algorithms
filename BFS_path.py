"""
Flood fill path finder (BFS)

. - grid col
x - visited col
S - start col
T - target col
# - obstacle
"""

from collections import deque
from pprint import pprint

target = (7, 7)
start = (1, 1)

grid = [[".", "#", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", "#", "#", ".", ".", "."],
        [".", "#", ".", "#", "#", "#", "#", ".", "."],
        [".", ".", ".", "#", ".", ".", "#", ".", "."],
        [".", "#", ".", "#", ".", ".", "#", ".", "."],
        [".", "#", ".", ".", ".", ".", "#", ".", "."],
        [".", "#", "#", ".", "#", "#", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."]]

height = len(grid)
width = len(grid[0])


def find_path_bfs(pos):
    q = deque()
    q.append(pos)
    came_from = {pos: None}

    while len(q) > 0:
        v_pos = q.popleft()

        neighbors = _get_neighbors(v_pos[0], v_pos[1])

        for neighbor in neighbors:
            if neighbor == target:
                came_from[neighbor] = v_pos
                _draw_path(came_from)
                return

            if neighbor not in came_from:
                q.append(neighbor)
                came_from[neighbor] = v_pos


def _get_neighbors(row, col):
    neighbors = []

    if col < width - 1 and grid[row][col + 1] != "#":
        neighbors.append((row, col + 1))
    if row < height - 1 and grid[row + 1][col] != "#":
        neighbors.append((row + 1, col))
    if col > 0 and grid[row][col - 1] != "#":
        neighbors.append((row, col - 1))
    if row > 0 and grid[row - 1][col] != "#":
        neighbors.append((row - 1, col))

    return neighbors


def _draw_path(came_from):
    current = came_from[target]
    path_length = 0

    # draw visited points
    for pos in came_from:
        if pos == start:
            grid[pos[0]][pos[1]] = "S"
        elif pos == target:
            grid[pos[0]][pos[1]] = "T"
        else:
            grid[pos[0]][pos[1]] = "x"

    # draw path
    while current != start:
        path_length += 1
        grid[current[0]][current[1]] = "@"
        current = came_from[current]

    pprint(grid)
    print(f"path length: {path_length}")

find_path_bfs(start)
