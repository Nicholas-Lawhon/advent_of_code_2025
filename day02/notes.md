# Part 1
- My initial thoughts are to split the number in half and compare the 2 sides
- The length of the number must be even
- If the length is even, we split it in half, and compare both sides (they should be equal)
- When we do the comparison, we should compare them as strings, not integers

# Part 2
- Now we need to find a way to check dynamic sequence lengths
- I know we need to calculate len(num) / 2, because that is the max sequence length of any given sequence
- We could iterate through the same number x times (max sequence length), but that seems slow (maybe it doesn't matter here though)
- Maybe a sliding window approach would work, checking each sequence one-by-one (up to the max sequence length)
- 
- An optimizzation we could make would be to NOT check each sequence length, but only those that divide by the len(n)
- Ex: If the len(n) is 10, we only need to check sequence lengths of 1, 2 and 5 (max sequence length). We can't have a sequence length of 3 or 4
-
- The Workflow:
- Get the total length of the string 
- Find all divisors of that length
- Only check those specific sequence lengths

# Parsing
- I think we should parse out the input into some type of tuple, representing start and end ranges
- We can store these as integers, and then we can easily iterate through the ranges