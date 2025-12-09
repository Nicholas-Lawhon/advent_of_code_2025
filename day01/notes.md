Part 1:

- The first problem to address is creating a "clock" so L1 at 0 leads to 99
I did a similar thing with a hashmap when solving the CodeCademy crypto challenges
I know there is a solution to this using the modulo (%) operator

- Will need a running counter to track every time 0 is hit

- When we parse for L or R directions, that will translate to either addition (R) or subtraction (L)

Overview:
- Start with clock position at 50
- We parse through the directions, applying the operation (R + or L -) and value to our current clock position (using % 100 to wrap around the clock)
- We then check if our current position == 0, and if so we increment our answer counter


Notes:
* First character is always direction

------------------------

Part 2:

- I believe we can use the modulo operator again here, to find how many times an operation would pass 0
- I'm thinking before each operation we can find the difference between current clock position and 100
- We then use the direction to get the operation used to find this number (R +, L -)
- That is our breaking point where we know if the operation value is at least that much, we'll hit 0
- However, I think we can use modulo with that number to get the "remainder", which is how MANY times we will be hitting 0

- We should start our operations by applying floor divsion of 100 to the steps.
- This tells us how many full circles we make around the clock, so we know the answer is AT LEAST that many
- Then, we take the remainder and apply that operation to the current position, and see if that passes 0 again


* I think I may need to apply the steps from the 1st operation before moving on to the remainder