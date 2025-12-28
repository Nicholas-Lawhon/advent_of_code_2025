from functools import reduce
from pathlib import Path
import operator
from typing import Callable


INPUT_FILE = Path(__file__).with_name("input.txt")


def parse_input() -> tuple[list[int], list[int], list[int], list[int], list[str]]:
    """Parse the input file into four rows of integers and one row of operations.

    Reads the input file and processes five lines:
    - Four rows of space-separated integers
    - One row of space-separated operation symbols

    Returns:
        A tuple containing:
            - row1: First row of integers
            - row2: Second row of integers
            - row3: Third row of integers
            - row4: Fourth row of integers
            - op_row: List of operation symbols ('+', '*', etc.)
    """
    raw_data = INPUT_FILE.read_text().splitlines()
    row1_raw, row2_raw, row3_raw, row4_raw, op_row_raw = raw_data

    row1 = list(map(int, row1_raw.split()))
    row2 = list(map(int, row2_raw.split()))
    row3 = list(map(int, row3_raw.split()))
    row4 = list(map(int, row4_raw.split()))
    op_row = op_row_raw.split()

    return row1, row2, row3, row4, op_row


def parse_input_part2() -> tuple[str, str, str, str, str]:
    """Parse the input file preserving spacing for Part 2.

    Returns the raw lines as strings with spacing preserved.
    Problems are separated by columns containing only spaces.

    Returns:
        A tuple containing:
            - row1_raw: First row as string with spacing preserved
            - row2_raw: Second row as string with spacing preserved
            - row3_raw: Third row as string with spacing preserved
            - row4_raw: Fourth row as string with spacing preserved
            - op_row_raw: Operations row as string with spacing preserved
    """
    raw_data = INPUT_FILE.read_text().splitlines()
    row1_raw, row2_raw, row3_raw, row4_raw, op_row_raw = raw_data
    return row1_raw, row2_raw, row3_raw, row4_raw, op_row_raw


def part01(
        row1: list[int], 
        row2: list[int], 
        row3: list[int], 
        row4: list[int], 
        op_row: list[str]
    ) -> int:
    """Calculate the sum of column-wise operations across four rows.

    For each column position, applies the specified operation to the four values
    from the same position in each row, then sums all results.

    Args:
        row1: First row of integers
        row2: Second row of integers
        row3: Third row of integers
        row4: Fourth row of integers
        op_row: List of operation symbols ('+' for addition, '*' for multiplication)

    Returns:
        The total sum of all column-wise operations
    """
    total_sum = 0
    operations: dict[str, Callable[[int, int], int]] = {
        "+": operator.add,
        "*": operator.mul
    }

    for i in range(len(op_row)):
        operation = operations[op_row[i]]
        current_nums = [row1[i], row2[i], row3[i], row4[i]]
        total = reduce(operation, current_nums)
        total_sum += total

    return total_sum


def part02() -> int:
    # I needed AI help w/ part 2
    # I was trying to use the original parsing function,
    # and was at a point that the logic was working but the answer was wrong
    # The AI was even stuck until I allowed it to look up the answer (very confusing problem)
    """Solve Part 2 by parsing with character-level precision.

    Problems are separated by columns containing only spaces.
    Within each problem, numbers are read right-to-left, column by column.
    """
    row1_raw, row2_raw, row3_raw, row4_raw, op_row_raw = parse_input_part2()

    operations = {
        "+": operator.add,
        "*": operator.mul
    }

    # Ensure all rows have the same length by padding with spaces
    max_len = max(len(row1_raw), len(row2_raw), len(row3_raw), len(row4_raw), len(op_row_raw))
    row1_raw = row1_raw.ljust(max_len)
    row2_raw = row2_raw.ljust(max_len)
    row3_raw = row3_raw.ljust(max_len)
    row4_raw = row4_raw.ljust(max_len)
    op_row_raw = op_row_raw.ljust(max_len)

    # Find column groups separated by all-space columns
    # A column is "all spaces" if all 4 data rows have a space at that position
    column_groups = []
    current_group_start = None

    for col_idx in range(max_len):
        is_all_spaces = (
            (col_idx >= len(row1_raw) or row1_raw[col_idx] == ' ') and
            (col_idx >= len(row2_raw) or row2_raw[col_idx] == ' ') and
            (col_idx >= len(row3_raw) or row3_raw[col_idx] == ' ') and
            (col_idx >= len(row4_raw) or row4_raw[col_idx] == ' ') and
            (col_idx >= len(op_row_raw) or op_row_raw[col_idx] == ' ')
        )

        if not is_all_spaces:
            if current_group_start is None:
                current_group_start = col_idx
        else:
            if current_group_start is not None:
                column_groups.append((current_group_start, col_idx))
                current_group_start = None

    # Don't forget the last group if it extends to the end
    if current_group_start is not None:
        column_groups.append((current_group_start, max_len))

    total_sum = 0

    # Process each column group from right to left
    for start_col, end_col in reversed(column_groups):
        # Extract this group's data
        group_row1 = row1_raw[start_col:end_col]
        group_row2 = row2_raw[start_col:end_col]
        group_row3 = row3_raw[start_col:end_col]
        group_row4 = row4_raw[start_col:end_col]
        group_op = op_row_raw[start_col:end_col].strip()

        # Build numbers by reading columns right-to-left
        current_problem_nums = []

        for col_pos in range(len(group_row1) - 1, -1, -1):
            curr_num = ""
            if col_pos < len(group_row1) and group_row1[col_pos] != " ":
                curr_num += group_row1[col_pos]
            if col_pos < len(group_row2) and group_row2[col_pos] != " ":
                curr_num += group_row2[col_pos]
            if col_pos < len(group_row3) and group_row3[col_pos] != " ":
                curr_num += group_row3[col_pos]
            if col_pos < len(group_row4) and group_row4[col_pos] != " ":
                curr_num += group_row4[col_pos]

            if curr_num:
                current_problem_nums.append(int(curr_num))

        # Apply the operation
        if current_problem_nums:
            operation = operations[group_op]
            total = reduce(operation, current_problem_nums)
            total_sum += total

    return total_sum

if __name__ == "__main__":
    row1, row2, row3, row4, op_row = parse_input()
    print("Part 1:", part01(row1, row2, row3, row4, op_row))
    print("Part 2:", part02())