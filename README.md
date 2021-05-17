# Error_handling.py

You given a simple task: write a function named division that takes a filename and prints the division result of each line

The file should have content similar to below:

6 a

5 2

3 0 

10 

15 2 abc
 
The printout should be:

Error: line contains non digits

2.5

Error: division by 0

Error: Too few numbers given

7.5
 
Please write the function in a way that all possible errors are handled gracefully (i.e try and except)
