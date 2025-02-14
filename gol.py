import curses
import random
import time

def initialize_grid(rows, cols, density=0.2):
    return [[1 if random.random() < density else 0 for _ in range(cols)] for _ in range(rows)]

def count_neighbors(grid, x, y):
    rows, cols = len(grid), len(grid[0])
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            count += grid[nx][ny]
    return count

def update_grid(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0] * cols for _ in range(rows)]
    for x in range(rows):
        for y in range(cols):
            neighbors = count_neighbors(grid, x, y)
            if grid[x][y] == 1 and (neighbors == 2 or neighbors == 3):
                new_grid[x][y] = 1
            elif grid[x][y] == 0 and neighbors == 3:
                new_grid[x][y] = 1
    return new_grid

def draw_grid(stdscr, grid):
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            stdscr.addch(x, y, "#" if cell else " ")
    stdscr.refresh()

def game_of_life(stdscr, rows=20, cols=40, delay=0.1):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(int(delay * 1000))
    grid = initialize_grid(rows, cols)
    
    while True:
        stdscr.erase()
        draw_grid(stdscr, grid)
        grid = update_grid(grid)
        time.sleep(delay)
        if stdscr.getch() == ord('q'):
            break

if __name__ == "__main__":
    curses.wrapper(game_of_life)
