How do you run my program:
	Go to your terminal and say "python3 cash.py" but make sure you're in the folder where it is contained first.
	Once inside, it will ask you how much change you require. Enter a value greater than 0.
	It will then tell you how many quarters, dimes, nickels, and pennies you need to distribute the change in the most efficient way possible.
	Congratulations!
Python Version: 3

A greedy algorithm is one who tries to stuff all the highest value things into a function first (like as I did with the quarters, i plugged all of them in that I could until
	i couldn't anymore to decrease the number of coins I would hand out overall). It is a funtion used to increase efficiency.

I Could have int-divided the change remaining by the integer value of the coin value (quarter = 25)(which would then be followed by subtracting the nmber of quarters*.25 from the change remaining)
 and used those numbers in my final answer instead of using while loops.

Huffman Encoding (compress data to the smallest amount), Dijkstra's Algorithm (find the shortest path through a gap). 
	It is simply an optimization algorithm, albeit one that does not always produce THE optimal solution