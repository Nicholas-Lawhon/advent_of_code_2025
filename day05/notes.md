# Parsing
- I think we should return 2 lists, fresh IDs and a list of ingredients to check
- We need to do all the str-int conversion in this parse function
- What we pass to the solutions should be ready-to-use data

# Part 1
- We take our fresh IDs, and check the ranges against the IDs to check
- We may need to turn our number ranges into an actual list of ints for each num
- We also need to convert IDs to check into a list of ints

- When check the IDs to check against the fresh IDs range, we need to convert the string into 2 seperate numbers
- - We will split the string at '-', and convert the min and max into an int
- - - Then we can check MIN <= ID <= MAX to verify it's fresh

# Part 2
- So we can ignore available IDs completely
- - We don't need to change parse_input(), we just pass only fresh_ids from main()

- The hard part is the fact that ranges overlap
- We can use a set() to include only uniques, but we have to make sure to include all valid ranges
- - Ex: 10 - 14, 16 - 20, 12 - 18 (Would include all nums 10-20)

- I'm thinking we can add all nums to a set
- - Then we really don't even need to worry about overlaps
- - - But we need to figure out how to unpack the ranges
- - - - Maybe we can use range(start, end + 1)

- It quickly became apparently that unpacking number ranges this long will NOT work
- - Instead, we need to keep a list of tuple ranges, and just add on to overlapping ranges
- - Ex: we have (2, 10) and (6, 15), the new range would be (2, 15)
- - - At the end, we can sum the difference between all tuples for a total count of unique IDs
- * It's important than we sort the list before we start this process *