"""Practical 1: Simple Reflex Agent in a two-location Vacuum World."""

def simple_reflex_agent(location, status):
    if status == 'Dirty':
        return 'Suck'
    elif location == 'A':
        return 'Right'
    else:
        return 'Left'

def run_vacuum_world(start_location, world, steps=6):
    location = start_location
    performance = 0
    for t in range(steps):
        status = world[location]
        action = simple_reflex_agent(location, status)
        print(f't={t} loc={location} status={status} action={action}')
        if action == 'Suck':
            world[location] = 'Clean'
        elif action == 'Right':
            location = 'B'
        elif action == 'Left':
            location = 'A'
        performance += sum(s == 'Clean' for s in world.values())
    return performance

if __name__ == '__main__':
    world = {'A': 'Dirty', 'B': 'Dirty'}
    print('Total performance:', run_vacuum_world('A', world))
