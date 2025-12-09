from pathlib import Path

INPUT_FILE = Path(__file__).with_name("input.txt")


def parse_input(raw):
    moves: list[tuple[str, int]] = []

    for line in raw.splitlines():
        if not line:
            continue

        direction = line[0].upper()
        value = ""

        for char in line:
            if char.isnumeric():
                value += char

        steps = int(value)
        moves.append((direction, steps))

    return moves

def part01(moves):
    clock_position = 50
    answer = 0

    for direction, steps in moves:
        if direction == "R":
            clock_position = (clock_position + steps) % 100
        elif direction == "L":
            clock_position = (clock_position - steps) % 100
        else:
            raise ValueError(f"Unexpected direction: {direction}")
        
        if clock_position == 0:
            answer += 1

    return answer

def part02(moves):
    clock_position = 50
    answer = 0

    # I was originally using math to solve this problem but got stuck on off-by-one issues
    # Simulating like this works only because our input size is small
    for direction, steps in moves:
        for _ in range(steps):
            if direction == "R":
                clock_position += 1
            elif direction == "L":
                clock_position -= 1
            else:
                raise ValueError(f"Unexpected direction: {direction}")

            if clock_position == 0:
                answer += 1
            
            # This is a noob way of handling wrap checking
            # Using the modulo (%) operator is MUCH cleaner
            if clock_position == 100:
                clock_position = 0
                answer += 1

            if clock_position == -1:
                clock_position = 99

    return answer


"""
------------------------------------------------------------------------
ALTERNATIVE SOLUTION (REFACTORED)
------------------------------------------------------------------------
This is a much cleaner and more pythonic way to solve this problem.

Python's modulo operator (%) handles negative numbers (e.g., -1 % 100 == 99),
allowing for a single line of logic to handle wrapping in both directions.

def part02_refactored(moves):
    clock_position = 50
    answer = 0

    for direction, steps in moves:
        # Determine if we are adding 1 (R) or subtracting 1 (L)
        delta = 1 if direction == "R" else -1

        for _ in range(steps):
            # Apply the move and the wrap in a single step
            clock_position = (clock_position + delta) % 100

            # Check if we landed on 0
            if clock_position == 0:
                answer += 1

    return answer
------------------------------------------------------------------------
"""


if __name__ == "__main__":
    raw = INPUT_FILE.read_text()
    moves = parse_input(raw)

    print("Part 1:", part01(moves))
    print("Part 2:", part02(moves))

# test_data = [("R", 30), ("L", 80), ("R", 50)]