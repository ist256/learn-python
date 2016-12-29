'''
Now You Code 3: CoinFlip Simulator

Write a program to simulate 100,000 coin flips. The program should output
the number of heads and tails.

For Example:
After 100000 flips. Heads: 50030, Tails 49970

Of course, since the flips are random, the counts will vary.

Your strategy should be to use a definite loop to flip a coin each time.
After you flip you should check for heads or tails and increment the count
accordingly.

HINT: Similar to the Rock, Paper, Scissors example, use random.choice() to
simulate coin flip.

Start out your program by writing your TODO list of steps
you'll need to solve the problem!
'''

# TODO: Write Todo list then beneath write your code


# Write code here (some provided for you)
import random
choices = ['heads','tails']
heads =0
tails =0
flips =100000
