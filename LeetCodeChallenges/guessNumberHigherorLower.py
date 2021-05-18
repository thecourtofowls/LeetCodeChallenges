# -*- coding: utf-8 -*-
"""
374. Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is 
higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible 
results:

-1: The number I picked is lower than your guess (i.e. pick < num).
1: The number I picked is higher than your guess (i.e. pick > num).
0: The number I picked is equal to your guess (i.e. pick == num).
Return the number that I picked.

Constraints:

1 <= n <= (2**31) - 1
1 <= pick <= n

Submitted Successfully
Created on Tue May 18 11:20:00 2021

@author: Christopher Obuchere
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        state_of = False
        start, end = 0, n
        mid = (start+end)//2
        while state_of == False:
            if guess(mid) == 0:
                state_of = True
            elif guess(mid) == 1:
                start = mid + 1 #raise mid
            else:
                end = mid - 1 #Reduce lowest
            mid = (start+end)//2
        return mid

