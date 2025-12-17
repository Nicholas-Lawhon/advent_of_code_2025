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


def part01(data):
    ans = 0

    for nums in data:
        num1 = 0
        num1_idx = 0
        num2 = 0

        for idx, num in enumerate(nums):
            if idx == len(nums) - 1:
                break

            if num > num1:
                num1 = num
                num1_idx = idx

        for idx, num in enumerate(nums):
            if idx <= num1_idx:
                continue

            if num > num2:
                num2 = num

        add_to_ans = str(num1) + str(num2)
        ans += int(add_to_ans)
    
    return ans


if __name__ == "__main__":
    data = parse_input()

    print("Part 1:", part01(data))