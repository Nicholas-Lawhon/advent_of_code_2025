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

# Part 2
- We need to iterate backwards and and build the number vertically
- We're going to have to construct the number ourselves by looking into the other rows on the same column
- We'll need a temp var to hold the number we're building, and a var for the current operation (num1 + num2 ...)

- We need to add zeros where needed to ensure all columns have matching lengths
- We can use the ljust string method to add padding to the right side
- We need to get the len of the num, and adjust padding for all numbers less
- We can convert to a string and do this operation, and then add the string char to a running 'current_num'
- This will allow us to build our number vertically and then convert to an int for the operation

* Important *
- It looks like the column alignment depends on the operation being performed
- So for addition we need to add padding to the right (.ljust)
- And for multiplication we need to add padding to the left (.rjust)