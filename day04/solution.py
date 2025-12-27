from pathlib import Path


INPUT_FILE = Path(__file__).with_name("input.txt")


def parse_input():
    grid: list[list[str]] = []
    raw_data = INPUT_FILE.read_text().strip().splitlines()

    for line in raw_data:
        if not line:
            continue

        row = list(line)
        grid.append(row)

    return grid



def part01(grid):
    rows = len(grid)
    cols = len(grid[0])
    accessible_rolls = 0

    directions = [
    (-1, -1), (-1, 0), (-1, 1),   # Top-Left, Top, Top-Right
    (0, -1),           (0, 1),    # Left,        Right
    (1, -1),  (1, 0),  (1, 1)     # Bottom-Left, Bottom, Bottom-Right
    ]

    # Loop through every row
    for r in range(rows):
        # Loop through every column
        for c in range(cols):

            # Check if the current position is a roll
            if grid[r][c] != '@':
                continue

            # Track how many neighbors are also rolls
            nearby_rolls_count = 0

            # Check all 8 directions
            for dr, dc in directions:
                # Calculate neighbor row and column
                nr = r + dr
                nc = c + dc
                
                # Out of bounds check
                if (nr < 0 or nr >= len(grid)) or (nc < 0 or nc >= len(grid[0])):
                    continue

                # If valid, check if grid[nr][nc] is '@'. If yes, increment nearby_roll_count
                if grid[nr][nc] == '@':
                    nearby_rolls_count += 1

            # After checking all 8 neighbors, apply the main rule
            # Rule: accessible if fewer than 4 adjacent rolls
            if nearby_rolls_count < 4:
                accessible_rolls += 1
                nearby_rolls_count = 0

    return accessible_rolls


def part02(grid):
    rows = len(grid)
    cols = len(grid[0])
    removed_rolls = 0
    grid_changed = True

    directions = [
    (-1, -1), (-1, 0), (-1, 1),   
    (0, -1),           (0, 1),    
    (1, -1),  (1, 0),  (1, 1)     
    ]

    while grid_changed == True:
        grid_changed = False
        
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] != '@':
                    continue

                nearby_rolls_count = 0

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    
                    if (nr < 0 or nr >= len(grid)) or (nc < 0 or nc >= len(grid[0])):
                        continue

                    if grid[nr][nc] == '@':
                        nearby_rolls_count += 1

                if nearby_rolls_count < 4:
                    grid[r][c] = 'X'
                    removed_rolls += 1
                    nearby_rolls_count = 0
                    grid_changed = True

    return removed_rolls

if __name__ == "__main__":
    data = parse_input()

    print("Part 01:", part01(data))
    print("Part 02:", part02(data))