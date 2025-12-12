# Part 1
- Initial thoughts are that we can iterate through the power banks and simply look for the largest numbers
- We need to assign higher priority to lower index numbers
- In the case of a tie, the lower index number should be selected (since we can't rearrange batteries)
- I know there's a better way, but I think we can iterate through the power bank twice
- On the first pass we store the highest number, and it's index, in a variable
- We then iterate from that index onward for the 2nd pass, storing the highest number in a 2nd variable
- We then turn those numbers into strings, add them, and then add that INT to our total answer value

# Parsing
- We need to store each line of the input file as a list of integers
- Each power bank (line) will have a return value that gets added to the answer variable
- So the file that we return from parse_input() should be a list[list[int]]