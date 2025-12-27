from pathlib import Path
import re


INPUT_FILE = Path(__file__).with_name("input.txt")


def parse_input():
    text = INPUT_FILE.read_text()

    fresh_id_ranges: list[tuple[int, int]] = []
    available_ids: list[int] = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        if "-" in line:
            left, right = line.split("-", 1)
            fresh_id_ranges.append((int(left), int(right)))
        else:
            available_ids.append(int(line))

    return fresh_id_ranges, available_ids


def part01(fresh_ids, available_ids):
    answer = 0

    for available_id in available_ids:
        for left, right in fresh_ids:
            if left <= available_id <= right:
                answer += 1
                break

    return answer


def part02(fresh_id_ranges):
    fresh_id_ranges.sort()

    current_start, current_end = fresh_id_ranges[0]
    total_fresh_ids_count = 0

    for start, end in fresh_id_ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            total_fresh_ids_count += (current_end - current_start + 1)
            current_start = start
            current_end = end

    total_fresh_ids_count += (current_end - current_start + 1)

    return total_fresh_ids_count


if __name__ == "__main__":
    fresh_ids, available_ids = parse_input()
    
    print("Part 01:", part01(fresh_ids, available_ids))
    print("Part 02:", part02(fresh_ids))