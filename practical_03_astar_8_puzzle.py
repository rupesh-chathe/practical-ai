"""Practical 3: A* Search for the 8-Puzzle using Manhattan distance."""

from heapq import heappush, heappop

GOAL = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
goal_pos = {}
for i in range(3):
    for j in range(3):
        goal_pos[GOAL[i][j]] = (i, j)

class Node:
    def __init__(self, state, parent=None, g=0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = self.heuristic()
        self.f = self.g + self.h

    def heuristic(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                value = self.state[i][j]
                if value != 0:
                    x, y = goal_pos[value]
                    distance += abs(i - x) + abs(j - y)
        return distance

    def __lt__(self, other):
        return self.f < other.f

def get_neighbors(state):
    neighbors = []
    x, y = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    state_list = [list(row) for row in state]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state_list]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))
    return neighbors

def print_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    path.reverse()
    print('\n=== Solution Path ===')
    for step, state in enumerate(path):
        print(f'Step {step}:')
        for row in state:
            print(row)
        print()
    print(f'Total Moves = {len(path) - 1}')

def astar(initial):
    open_list = []
    visited = set()
    heappush(open_list, Node(initial))
    while open_list:
        current = heappop(open_list)
        if current.state == GOAL:
            print_path(current)
            return
        if current.state in visited:
            continue
        visited.add(current.state)
        for neighbor in get_neighbors(current.state):
            if neighbor not in visited:
                heappush(open_list, Node(neighbor, current, current.g + 1))
    print('No Solution Found')

if __name__ == '__main__':
    initial = ((1, 2, 3), (4, 0, 6), (7, 5, 8))
    astar(initial)
