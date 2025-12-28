from functools import reduce
from pathlib import Path
import operator


INPUT_FILE = Path(__file__).with_name("input.txt")


def parse_input():
    raw_data = INPUT_FILE.read_text().splitlines()
    row1_raw, row2_raw, row3_raw, row4_raw, op_row_raw = raw_data

    row1 = list(map(int, row1_raw.split()))
    row2 = list(map(int, row2_raw.split()))
    row3 = list(map(int, row3_raw.split()))
    row4 = list(map(int, row4_raw.split()))
    op_row = op_row_raw.split()

    return row1, row2, row3, row4, op_row


def part01(row1, row2, row3, row4, op_row):
    total_sum = 0
    operations = {
        "+": operator.add,
        "*": operator.mul
    }

    for i in range(len(op_row)):
        operation = operations.get(op_row[i])
        current_nums = [row1[i], row2[i], row3[i], row4[i]]
        total = reduce(operation, current_nums)
        total_sum += total

    return total_sum


def part02(data):
    pass


if __name__ == "__main__":
    row1, row2, row3, row4, op_row = parse_input()

    print("Part 1:", part01(row1, row2, row3, row4, op_row))
    #print("Part 2:", part02(data))