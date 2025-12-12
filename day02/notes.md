- My initial thoughts are to split the number in half and compare the 2 sides
- The length of the number must be even
- If the length is even, we split it in half, and compare both sides (they should be equal)
- When we do the comparison, we should compare them as strings, not integers

# Parsing
- I think we should parse out the input into some type of tuple, representing start and end ranges
- We can store these as integers, and then we can easily iterate through the ranges