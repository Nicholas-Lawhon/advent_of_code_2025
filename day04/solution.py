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



def part01(data):
    directions = [
    (-1, -1), (-1, 0), (-1, 1),   # Top-Left, Top, Top-Right
    (0, -1),           (0, 1),    # Left,        Right
    (1, -1),  (1, 0),  (1, 1)     # Bottom-Left, Bottom, Bottom-Right
]
    
    for i in data:
        print(i)



def part02(data):
    pass



if __name__ == "__main__":
    data = parse_input()

    print("Part 01:", part01(data))