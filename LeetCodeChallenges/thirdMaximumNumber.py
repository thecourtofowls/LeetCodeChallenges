# -*- coding: utf-8 -*-
"""
414. Third Maximum Number

Given integer array nums, return the third maximum number in this array. 
If the third maximum does not exist, return the maximum number.

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

Submitted Successfully
Created on Mon May 17 17:18:13 2021

@author: Christopher Obuchere
"""
from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        self.list_len = len(nums)
        
        self.up = (10**4)
        self.down = 1
        self.up_n = (2**31)-1
        self.down_n = -(2**31)
        em_list = []
        
        if ( (self.list_len >= self.down) & (self.list_len <= self.up) & 
            all(k <= self.up_n for k in nums) & all(k >= self.down_n for k in nums)):
            for x in nums:
                if x in em_list:
                    continue
                else:
                    em_list.append(x)
            nums[:] = em_list
            
            if (len(nums) == 1):
                third_max = nums[0]
            elif (len(nums) == 2):
                third_max = max(nums)
            else:
                third_max = sorted(nums)[len(nums)-3]

            return third_max
        
k = Solution()
k.thirdMax(nums = [1,2,2,5,3,5])