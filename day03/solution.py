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


def part02(data):
    ans = 0
    add_to_ans = 0

    for nums in data:
        add_to_ans = ""
        idx_start = 0

        while len(add_to_ans) < 12:
            idx_end = len(nums) - (12 - len(add_to_ans)) + 1
            highest_num = 0
            highest_idx = 0

            for i in range(idx_start, idx_end):
                if nums[i] > highest_num:
                    highest_num = nums[i]
                    highest_idx = i

            idx_start = highest_idx + 1
            add_to_ans = add_to_ans + str(highest_num)

        ans += int(add_to_ans)
            
    return ans



if __name__ == "__main__":
    data = parse_input()

    print("Part 1:", part01(data))
    print("Part 2:", part02(data))