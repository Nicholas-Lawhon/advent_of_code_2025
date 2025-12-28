# Parsing
- We need to seperate each line into it's own list (so 4 lists total)
- We'll return either 4 list[int] and 1 list[str] (representing the operations)
- - Or we'll return 4 list[tuple[int]] and 1 list[tuple[str]]

# Part 1
- Maybe we can iterate through the nums and create a list of tuples for each column of nums
- We then repeat this for all 4 num lines, plus the final operations line (+ or *)
- We end up with 5 different lists of tuples, and we can line those up to perform the operations
- - For ex: we can iterate through a range(len(nums)), and use indicies to operate on the correct columns
- * We may not need to use tuples, a list of ints may also work *
- We will need to convert a string of operations into the actual mathmatical operation