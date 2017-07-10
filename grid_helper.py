import math

START_COL = "S"
END_COL = "E"
VISITED_COL = "x"
OBSTACLE_COL = "#"
PATH_COL = "@"


def generate_grid0():
    return [[".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."]]


def generate_grid1():
    return [[".", ".", "#", ".", ".", ".", ".", ".", "."],
            [".", ".", "#", ".", "#", ".", ".", ".", "."],
            [".", ".", ".", ".", "#", ".", ".", ".", "."],
            [".", ".", "#", ".", "#", ".", ".", ".", "."],
            [".", ".", "#", ".", ".", ".", ".", ".", "."],
            [".", ".", "#", ".", "#", ".", ".", ".", "."],
            [".", ".", "#", "#", "#", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."]]


def generate_grid():
    """
    worst obstacle for B*
    """

    return [[".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "#", "#", "#", "#", "#", "#", "#", "."],
            [".", ".", ".", ".", ".", ".", ".", "#", "."],
            [".", ".", ".", ".", ".", ".", ".", "#", "."],
            [".", ".", ".", ".", ".", ".", ".", "#", "."],
            [".", ".", ".", ".", ".", ".", ".", "#", "."],
            [".", ".", ".", ".", ".", ".", ".", "#", "."],
            [".", "#", "#", "#", "#", "#", "#", "#", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."]]


def generate_grid_w():
    """
    weighted grid
    """

    return [[".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "#", "#", "#", "#", ".", "#", "#", "."],
            [".", ".", "8", "1", "1", ".", ".", "#", "."],
            [".", ".", "2", "7", "1", ".", ".", "#", "."],
            [".", ".", "2", "7", "4", ".", ".", "#", "."],
            [".", ".", "2", "7", "1", ".", ".", "#", "."],
            [".", ".", ".", "5", "1", ".", ".", "#", "."],
            [".", "#", "#", "#", "#", "#", "#", "#", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."]]


def heuristic_distance(pos, end_pos, type="e"):
    """
    m - manhattan
    e - euclidean
    """

    dx = abs(pos[0] - end_pos[0])
    dy = abs(pos[1] - end_pos[1])

    if type == "m":
        return dx + dy

    return math.sqrt(dx * dx + dy * dy)


def find_path(start, end, came_from):
    """Find the shortest path from start to end point"""

    path = [end]

    current = end
    while current != start:
        current = came_from[current]
        path.append(current)

    # reverse to have Start -> Target
    # just looks nicer
    path.reverse()

    return path


def get_weight(grid, pos):
    col_val = grid[pos[0]][pos[1]]
    return int(col_val) if col_val.isdigit() else 1


def get_neighbors(grid, row, col):
    height = len(grid)
    width = len(grid[0])

    neighbors = [(row + 1, col), (row, col - 1), (row - 1, col), (row, col + 1)]

    # make path nicer
    if (row + col) % 2 == 0:
        neighbors.reverse()

    # check borders
    neighbors = filter(lambda t: (0 <= t[0] < height and 0 <= t[1] < width), neighbors)
    # check obstacles
    neighbors = filter(lambda t: (grid[t[0]][t[1]] != OBSTACLE_COL), neighbors)

    return neighbors


def draw_path(path, grid):
    for row, col in path:
        grid[row][col] = PATH_COL

    # draw start and end
    start_pos = path[0]
    end_pos = path[-1]
    grid[start_pos[0]][start_pos[1]] = START_COL
    grid[end_pos[0]][end_pos[1]] = END_COL

    return grid