# -*- coding: utf-8 -*-
"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while 
maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Constraints:

1 <= nums.length <= (10**4)
-(2**31) <= nums[i] <= (2**31) - 1

Submitted Successfully
Created on Mon May 17 15:36:20 2021

@author: Christopher Obuchere
"""

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.list_len = len(nums)
        
        self.up = (10**4)
        self.down = 1
        self.up_n = (2**31)-1
        self.down_n = -(2**31)
        
        if ( (self.list_len >= self.down) & (self.list_len <= self.up) & 
            all(k <= self.up_n for k in nums) & all(k >= self.down_n for k in nums)):
            nums[:] =  [x for x in nums if x != 0]
            nums[:] = nums + [0]*(self.list_len-len(nums))
            

#TEst
k = Solution()
k.moveZeroes(nums = [0,1,2,2,3,0,4,2])