"""Practical 2: Model-Based Agent navigating a grid with obstacles."""

class GridEnvironment:
    def __init__(self, size, obstacles, start, goal):
        self.size = size
        self.obstacles = set(obstacles)
        self.start = start
        self.goal = goal

    def is_inside(self, cell):
        r, c = cell
        return 0 <= r < self.size and 0 <= c < self.size

    def sense_neighbours(self, pos):
        r, c = pos
        directions = {
            'Up': (r - 1, c), 'Down': (r + 1, c),
            'Left': (r, c - 1), 'Right': (r, c + 1),
        }
        percepts = {}
        for cell in directions.values():
            if not self.is_inside(cell):
                continue
            percepts[cell] = 'Obstacle' if cell in self.obstacles else 'Free'
        return percepts

class ModelBasedAgent:
    def __init__(self, start, goal):
        self.pos = start
        self.goal = goal
        self.known_cells = {start: 'Free'}
        self.visited = {start}
        self.path_history = [start]

    def update_model(self, percepts):
        for cell, status in percepts.items():
            self.known_cells[cell] = status

    def choose_action(self):
        r, c = self.pos
        moves = {
            'Up': (r - 1, c), 'Down': (r + 1, c),
            'Left': (r, c - 1), 'Right': (r, c + 1),
        }
        for name, cell in moves.items():
            if self.known_cells.get(cell) == 'Free' and cell not in self.visited:
                return name, cell
        if len(self.path_history) > 1:
            self.path_history.pop()
            return 'Backtrack', self.path_history[-1]
        return 'No Path Found', self.pos

    def step(self, environment):
        percepts = environment.sense_neighbours(self.pos)
        self.update_model(percepts)
        if self.pos == self.goal:
            return 'Goal reached'
        action, next_cell = self.choose_action()
        if action == 'No Path Found':
            return 'Failed: Trapped'
        self.pos = next_cell
        if action != 'Backtrack':
            self.visited.add(next_cell)
            self.path_history.append(next_cell)
        return action

def print_known_cells(known_cells, items_per_line=3):
    sorted_cells = sorted(known_cells.items())
    entries = [f"{cell}: '{status}'" for cell, status in sorted_cells]
    print('{')
    for i in range(0, len(entries), items_per_line):
        line = ', '.join(entries[i:i + items_per_line])
        if i + items_per_line < len(entries):
            line += ','
        print(' ' + line)
    print('}')

if __name__ == '__main__':
    grid_size = 5
    start_pos = (0, 0)
    goal_pos = (4, 4)
    obstacles = [(1, 1), (1, 2), (2, 3), (3, 0), (3, 3)]
    env = GridEnvironment(grid_size, obstacles, start_pos, goal_pos)
    agent = ModelBasedAgent(start_pos, goal_pos)
    for step_count in range(1, 51):
        result = agent.step(env)
        if result == 'Goal reached':
            print(f'Goal reached at step {step_count}!\n')
            break
        if result == 'Failed: Trapped':
            print('No path found.\n')
            break
    else:
        print('Maximum steps reached.\n')
    print("Agent's route to find goal:")
    print_known_cells(agent.known_cells)
