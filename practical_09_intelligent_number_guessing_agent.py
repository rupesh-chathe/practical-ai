"""Practical 9: Intelligent number-guessing agent using higher/lower hints."""

def intelligent_guessing_agent():
    print('=' * 50)
    print('      INTELLIGENT NUMBER-GUESSING AGENT')
    print('=' * 50)
    print('\nThink of a secret number between 1 and 100.')
    print('Provide feedback to the agent using:')
    print(" 'H' -> if your number is HIGHER than the guess")
    print(" 'L' -> if your number is LOWER than the guess")
    print(" 'C' -> if the guess is CORRECT\n")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        feedback = input(
            f'Attempt {attempts}: Is your number {guess}? (H/L/C): '
        ).strip().upper()

        if feedback == 'C':
            print('\n' + '=' * 50)
            print(f' SUCCESS! Agent guessed your number {guess} in {attempts} attempts.')
            print('=' * 50)
            break
        elif feedback == 'H':
            low = guess + 1
        elif feedback == 'L':
            high = guess - 1
        else:
            print("Invalid input! Please enter 'H', 'L', or 'C'.")
            attempts -= 1

        if low > high:
            print('\n' + '!' * 50)
            print(' Error: Inconsistent feedback detected!')
            print(' Please restart and provide correct hints.')
            print('!' * 50)
            break

if __name__ == '__main__':
    intelligent_guessing_agent()
