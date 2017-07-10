from pprint import pprint
import collections

grid = [[".", ".", ".", ".", ".", ".", ".", ],
        [".", ".", ".", "#", "#", ".", ".", ],
        [".", ".", "#", ".", "#", ".", ".", ],
        [".", ".", "#", ".", "#", ".", ".", ],
        [".", ".", "#", ".", "#", ".", ".", ],
        [".", ".", "#", ".", "#", ".", ".", ],
        [".", ".", ".", "#", ".", ".", ".", ],
        [".", ".", ".", ".", ".", ".", ".", ],
        [".", ".", ".", ".", ".", ".", ".", ]]

height = len(grid)
width = len(grid[0])

START_COL = "S"
VISITED_COL = "x"
OBSTACLE_COL = "#"


def _get_neighbors(row, col):
    neighbors = []

    if col < width - 1 and grid[row][col + 1] != OBSTACLE_COL:
        neighbors.append((row, col + 1))
    if row < height - 1 and grid[row + 1][col] != OBSTACLE_COL:
        neighbors.append((row + 1, col))
    if col > 0 and grid[row][col - 1] != OBSTACLE_COL:
        neighbors.append((row, col - 1))
    if row > 0 and grid[row - 1][col] != OBSTACLE_COL:
        neighbors.append((row - 1, col))

    return neighbors


def flood_fill_recursion(row, col):
    if row < 0 or row >= height or col < 0 or col >= width:
        return

    if grid[row][col] != ".":
        return

    grid[row][col] = VISITED_COL
    flood_fill_recursion(row + 1, col)
    flood_fill_recursion(row - 1, col)
    flood_fill_recursion(row, col - 1)
    flood_fill_recursion(row, col + 1)


flood_fill_recursion(1, 1)
print("flood_fill_recursion")
pprint(grid)


def flood_fill_queue(row, col, target, replacement):
    q = collections.deque()

    if grid[row][col] != target:
        return

    grid[row][col] = replacement
    q.append((row, col))

    while len(q) > 0:
        pos = q.popleft()

        if pos[0] > 0 and grid[pos[0] - 1][pos[1]] == target:
            grid[pos[0] - 1][pos[1]] = replacement
            q.append((pos[0] - 1, pos[1]))
        if pos[0] < height - 1 and grid[pos[0] + 1][pos[1]] == target:
            grid[pos[0] + 1][pos[1]] = replacement
            q.append((pos[0] + 1, pos[1]))
        if pos[1] < width - 1 and grid[pos[0]][pos[1] + 1] == target:
            grid[pos[0]][pos[1] + 1] = replacement
            q.append((pos[0], pos[1] + 1))
        if pos[1] > 0 and grid[pos[0]][pos[1] - 1] == target:
            grid[pos[0]][pos[1] - 1] = replacement
            q.append((pos[0], pos[1] - 1))


# flood_fill_queue(2, 5, 0, 3)
print("flood_fill_queue")
pprint(grid)


def flood_fill_stack(row, col, target, replacement):
    stack = []

    if grid[row][col] != target:
        return

    grid[row][col] = replacement
    stack.append((row, col))

    while len(stack) > 0:
        pos = stack.pop()

        if pos[0] > 0 and grid[pos[0] - 1][pos[1]] == target:
            grid[pos[0] - 1][pos[1]] = replacement
            stack.append((pos[0] - 1, pos[1]))
        if pos[0] < height - 1 and grid[pos[0] + 1][pos[1]] == target:
            grid[pos[0] + 1][pos[1]] = replacement
            stack.append((pos[0] + 1, pos[1]))
        if pos[1] < width - 1 and grid[pos[0]][pos[1] + 1] == target:
            grid[pos[0]][pos[1] + 1] = replacement
            stack.append((pos[0], pos[1] + 1))
        if pos[1] > 0 and grid[pos[0]][pos[1] - 1] == target:
            grid[pos[0]][pos[1] - 1] = replacement
            stack.append((pos[0], pos[1] - 1))


# flood_fill_stack(2, 5, 0, 3)
print("flood_fill_stack")
pprint(grid)


def flood_fill_set(row, col):
    visited = set()

    visited.add((row, col))

    while len(visited) > 0:
        pos = visited.pop()

        neighbors = _get_neighbors(pos[0], pos[1])

        for neighbor in neighbors:
            if grid[neighbor[0]][neighbor[1]] != VISITED_COL:
                visited.add(neighbor)
                grid[neighbor[0]][neighbor[1]] = VISITED_COL

    grid[row][col] = START_COL

flood_fill_set(1, 1)
print("flood_fill_set")
pprint(grid)

