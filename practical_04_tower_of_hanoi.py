"""Practical 4: Tower of Hanoi using recursion."""

def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f'Move Disk 1 from {source} to {destination}')
        return
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f'Move Disk {n} from {source} to {destination}')
    tower_of_hanoi(n - 1, auxiliary, source, destination)

if __name__ == '__main__':
    n = int(input('Enter number of disks: '))
    if n < 1:
        print('Please enter a positive number of disks.')
    else:
        print('\nSequence of Moves:\n')
        tower_of_hanoi(n, 'A', 'B', 'C')
