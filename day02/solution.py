from pathlib import Path

INPUT_FILE = Path(__file__).with_name("input.txt")


def parse_input():
    ranges: list[tuple[int, int]] = []
    
    with open(INPUT_FILE) as f:
        raw_data = f.read().strip()

    range_strings = raw_data.split(',')

    for item in range_strings:
        parts = item.split('-')

        start_val = int(parts[0])
        end_val = int(parts[1])

        current_range = (start_val, end_val)
        ranges.append(current_range)

    return ranges


def part01(ranges):
    answer = 0
    
    for i in ranges:
        for n in range(i[0], i[1] + 1):
            n_string = str(n)
            breakpoint = len(n_string) // 2

            if len(n_string) % 2 != 0:
                continue

            if n_string[:breakpoint] == n_string[breakpoint:]:
                answer += n

    return answer


def part02(ranges):
    answer = 0

    for i in ranges:
        for n in range(i[0], i[1] + 1):
            n_string = str(n)
            n_s_len = len(n_string)
            max_sequence_length = n_s_len // 2

            for seq_len in range(1, max_sequence_length + 1):
                if n_s_len % seq_len != 0:
                    continue

                pattern = n_string[:seq_len]
                reconstructed = pattern * (n_s_len // seq_len)

                if reconstructed == n_string:
                    answer += int(n_string)
                    break

    return answer


if __name__ == "__main__":
    data = parse_input()

    print("Part 1:", part01(data))
    print("Part 2:", part02(data))