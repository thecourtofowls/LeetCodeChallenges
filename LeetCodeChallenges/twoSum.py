# -*- coding: utf-8 -*-
"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the 
same element twice.

Constraints:

2 <= nums.length <= 10**3
-10**9 <= nums[i] <= 10**9
-10**9 <= target <= 10**9
Only one valid answer exists.


Created on Sat Feb 20 16:55:46 2021

@author: christopher obuchere
"""
#
nums = [2,7,11,15, 100000000000000]
nums = [3,2,4,5]
nums = [3,2,4]
nums = [3,3]
nums = [5,4]
nums = [9]
#
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        self._data_len = len(nums)
        self.solution = []

        if ((len(self.nums) >= 2) & (self.target <= 10**9) & (self.target >= -10**9 ) & 
            all(k <= 10**9 for k in self.nums) & all(k >= -10**9 for k in self.nums)):
            self.i = 0
            while self.i < len(self.nums):
                for x in range(self._data_len):
                    if ((self.nums[self.i] + self.nums[x] == self.target) & (self.i != x)):
                        for pos in [self.i,x]:
                            if pos not in self.solution:
                                self.solution.append(pos)
                self.i = self.i + 1
            return self.solution[:]
        else:
            raise Exception("Either 'Not a list' or 'Target and List contents fail constraints'.")
            
k = Solution()
k.twoSum(nums = nums, target = 6)

