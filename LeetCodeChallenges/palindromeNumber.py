# -*- coding: utf-8 -*-
"""
9. Palindrome Number
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. 
For example, 121 is palindrome while 123 is not.

Constraints:

-(2**31) <= x <= (2**31) - 1

Submitted Successfully
Created on Thu May 20 15:22:57 2021

@author: Christopher Obuchere
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        self.list_num = [y for y in str(x)]
        self.rev_list = self.list_num[::-1]
        
        if (self.list_num == self.rev_list):
            return True
        else:
            return False

k = Solution()
k.isPalindrome(x = 121)