"""Practical 5: BFS shortest path for robot movement in a 5x5 grid."""

from collections import deque

# 0 = Free cell; 1 = Obstacle
GRID = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
]
SOURCE = (0, 0)
DESTINATION = (4, 4)

def bfs(grid, source, destination):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(source, [source])])
    visited = {source}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        current, path = queue.popleft()
        print('Visiting:', current)
        if current == destination:
            return path
        r, c = current
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            next_cell = (nr, nc)
            if (0 <= nr < rows and 0 <= nc < cols and
                    grid[nr][nc] == 0 and next_cell not in visited):
                visited.add(next_cell)
                queue.append((next_cell, path + [next_cell]))
    return None

if __name__ == '__main__':
    path = bfs(GRID, SOURCE, DESTINATION)
    print('\nShortest Path:')
    if path:
        for cell in path:
            print(cell)
        print('\nNumber of moves:', len(path) - 1)
    else:
        print('No path found')
