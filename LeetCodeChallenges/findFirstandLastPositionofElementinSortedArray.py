# -*- coding: utf-8 -*-
"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting 
and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
Constraints:

0 <= nums.length <= (10**5)
-(10**9) <= nums[i] <= (10**9)
nums is a non-decreasing array.
-(10**9) <= target <= (10**9)

Submitted Successfully
Created on Tue May 18 12:00:30 2021

@author: Christopher Obuchere
"""

from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        self.list_len = len(nums)
        
        self.set_list = set(nums)
        self.set_len = len(self.set_list)
        
        self.up = (10**5)
        self.down = 0
        
        self.up_t = (10**9)
        self.down_t = -(10**9)
        
        if ( (self.list_len >= self.down) & (self.list_len <= self.up) & 
            (target >= self.down_t) & (target <= self.up) & 
            all(k <= self.up_t for k in nums) & all(k >= self.down_t for k in nums)):
            
            index_target = [i for i, e in enumerate(nums) if e == target]
            if (len(index_target) == 1):
                return index_target+index_target
            elif (len(index_target) == 2):
                return index_target
            elif (len(index_target) >= 3):
                index_target[:] = [index_target[0], index_target[-1]]
                return index_target
            else:
                return [-1,-1]
            
k = Solution()
k.searchRange(nums = [5,7,7,8,8,10], target = 1)