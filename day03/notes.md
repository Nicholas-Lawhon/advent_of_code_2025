# Part 1
- Initial thoughts are that we can iterate through the power banks and simply look for the largest numbers
- We need to assign higher priority to lower index numbers
- In the case of a tie, the lower index number should be selected (since we can't rearrange batteries)
- I know there's a better way, but I think we can iterate through the power bank twice
- On the first pass we store the highest number, and it's index, in a variable
- We then iterate from that index onward for the 2nd pass, storing the highest number in a 2nd variable
- We then turn those numbers into strings, add them, and then add that INT to our total answer value

# Option 2
- If we wanted to iterate once, we could use 2 counters to track the highest 2 numbers and their index
- We then check if current number is higher than num1 or num2
- We checking for num2, if current number index == num1 index, we skip
- That should ensure that we get the 2 highest numbers without assigning the same index to num1 and num2

# Parsing
- We need to store each line of the input file as a list of integers
- Each power bank (line) will have a return value that gets added to the answer variable
- So the file that we return from parse_input() should be a list[list[int]]

# Part 2
- My initial thoughts are to iterate in reverse, starting at the 12th index from the end
- We could then slide the window as we come across a num that is >= num1
- The problem is, I'm not sure how I check each suseqent number in the window without tracking 12 different variables
- I could make a first pass ending at len(nums) - 13, and use that idx to start the next iteration
- - But then I would still need a way to track the other numbers

- What if I sum the numbers in my 12 digit window as it slides?
- - The problem is how to skip digits and expand the window non-sequentially 

- I could use a while loop to continously iterate until all possible combinations have been searched
- 