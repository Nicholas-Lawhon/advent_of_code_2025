# Day 6 Part 2 - Understanding the Solution

## The Problem We Had

Initially, we were getting an answer of **11090355539291** which was **too high**. The issue was in how we were parsing and grouping the input data.

## What We Were Doing Wrong

### Incorrect Parsing Approach

We were using Python's `.split()` method to parse the input:

```python
# WRONG APPROACH
row1 = list(map(int, row1_raw.split()))  # [617, 828, 937, 2344, 145, ...]
row2 = list(map(int, row2_raw.split()))  # [478, 337, 998, 3442, 618, ...]
op_row = op_row_raw.split()              # ['*', '+', '*', '+', '+', ...]
```

This approach **destroys the spacing information** in the input! When you call `.split()`, Python splits on any whitespace and removes all spacing between numbers.

### Why This Was Wrong

Looking at the raw input:
```
617 828 937 2344 145 37   83  845 37   7 882
```

Notice there are **different amounts of spaces** between numbers:
- Single space between `617` and `828`
- Single space between `828` and `937`
- **Three spaces** between `37` and `83`
- **Two spaces** between `83` and `845`

These multi-space gaps are **intentional separators** that mark the boundaries between different problems!

### What We Were Treating as the Input

We thought each number was its own separate problem column, giving us 1000 individual problems. We would then pad each column's numbers and read them vertically.

For example, we treated column index 0 as one problem with numbers [617, 478, 48, 44] and operator '*'.

## What the Problem Actually Wanted

### The Key Insight: Column Groups

**Problems are separated by columns containing ONLY spaces across all rows.**

Let's look at the example from the problem:

```
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
```

If we look at this character-by-character:

```
Position: 0123456789012345
Row1:     123 328  51 64
Row2:      45 64  387 23
Row3:       6 98  215 314
OpRow:    *   +   *   +
```

Notice the patterns:
- Positions 0-2: Contains numbers (123, 45, 6)
- **Position 3: ALL SPACES** ← Separator!
- Positions 4-6: Contains numbers (328, 64, 98)
- **Position 7: ALL SPACES** ← Separator!
- Positions 8-10: Contains numbers (51, 387, 215)
- **Position 11: ALL SPACES** ← Separator!
- Positions 12-14: Contains numbers (64, 23, 314)

So there are actually **4 separate problems**, not one problem per number!

### Problem Groups

1. **Group 1** (columns 0-2): `123`, `45`, `6` with operator `*`
2. **Group 2** (columns 4-6): `328`, `64`, `98` with operator `+`
3. **Group 3** (columns 8-10): `51`, `387`, `215` with operator `*`
4. **Group 4** (columns 12-14): `64`, `23`, `314` with operator `+`

## How We Fixed It

### Step 1: Preserve Spacing in Parsing

We created a new parser that keeps the raw strings intact:

```python
def parse_input_part2() -> tuple[str, str, str, str, str]:
    """Parse the input file preserving spacing for Part 2."""
    raw_data = INPUT_FILE.read_text().splitlines()
    row1_raw, row2_raw, row3_raw, row4_raw, op_row_raw = raw_data
    return row1_raw, row2_raw, row3_raw, row4_raw, op_row_raw
```

Now we have strings like:
```python
row1_raw = "617 828 937 2344 145 37   83  845 37   7 882..."
```

### Step 2: Identify Column Groups

We iterate through each character position and check if ALL rows have a space at that position:

```python
# Ensure all rows have the same length
max_len = max(len(row1_raw), len(row2_raw), len(row3_raw), len(row4_raw), len(op_row_raw))
row1_raw = row1_raw.ljust(max_len)
row2_raw = row2_raw.ljust(max_len)
row3_raw = row3_raw.ljust(max_len)
row4_raw = row4_raw.ljust(max_len)
op_row_raw = op_row_raw.ljust(max_len)

# Find column groups separated by all-space columns
column_groups = []
current_group_start = None

for col_idx in range(max_len):
    # Check if this column position is ALL spaces across all rows
    is_all_spaces = (
        row1_raw[col_idx] == ' ' and
        row2_raw[col_idx] == ' ' and
        row3_raw[col_idx] == ' ' and
        row4_raw[col_idx] == ' ' and
        op_row_raw[col_idx] == ' '
    )

    if not is_all_spaces:
        # Start of a new group or continuation of current group
        if current_group_start is None:
            current_group_start = col_idx
    else:
        # All-space column - end current group if we're in one
        if current_group_start is not None:
            column_groups.append((current_group_start, col_idx))
            current_group_start = None

# Don't forget the last group
if current_group_start is not None:
    column_groups.append((current_group_start, max_len))
```

For our input, this finds exactly **1000 column groups** (problems), not 1000 individual columns!

### Step 3: Process Each Group Right-to-Left

For each group, we read the numbers by iterating through column positions **right-to-left** and building numbers by concatenating digits **top-to-bottom**:

```python
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
        # Read top-to-bottom to build each number
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
```

## Example Walkthrough

Let's trace through the rightmost problem from the example:

```
Group data (columns 12-14):
  group_row1 = "64 "
  group_row2 = "23 "
  group_row3 = "314"
  group_op = "+"
```

Reading **right-to-left** (positions 2, 1, 0):

**Position 2 (rightmost):**
- row1[2] = ' ' (space) → skip
- row2[2] = ' ' (space) → skip
- row3[2] = '4' → curr_num = "4"
- Result: **4**

**Position 1:**
- row1[1] = '4' → curr_num = "4"
- row2[1] = '3' → curr_num = "43"
- row3[1] = '1' → curr_num = "431"
- Result: **431**

**Position 0:**
- row1[0] = '6' → curr_num = "6"
- row2[0] = '2' → curr_num = "62"
- row3[0] = '3' → curr_num = "623"
- Result: **623**

Numbers for this problem: `[4, 431, 623]`

Operation: `4 + 431 + 623 = 1058` ✓

## The Difference in Results

### Old Approach (Wrong)
- Treated each `.split()` result as a separate problem
- Got 1000 problems, but they were the wrong problems
- Answer: **11090355539291** (too high)

### New Approach (Correct)
- Identified column groups separated by all-space columns
- Got 1000 problems, but they were the RIGHT problems
- Answer: **11044319475191** ✓

## Key Takeaway

**Always preserve the original formatting of the input when spacing might be significant!**

Using `.split()` is convenient, but it destroys information about spacing. For this problem, the spacing was **critical** to understanding which numbers belonged together in the same problem.

The fix required:
1. Reading raw strings without `.split()`
2. Identifying column boundaries by finding all-space columns
3. Processing each group as a separate problem
