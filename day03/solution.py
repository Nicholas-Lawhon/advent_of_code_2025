from pathlib import Path


INPUT_FILE = Path(__file__).with_name("input.txt")


def parse_input():
    power_banks: list[list[int]] = []
    raw_data = INPUT_FILE.read_text().strip()

    for line in raw_data.splitlines():
        if not line:
            continue

        row = [int(char) for char in line]
        power_banks.append(row)

    return power_banks

data = parse_input()

print(data[0])
print(data[0][0])