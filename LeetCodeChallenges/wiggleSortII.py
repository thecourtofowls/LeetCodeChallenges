# -*- coding: utf-8 -*-
"""
324. Wiggle Sort II

Given an integer array nums, reorder it such that 
nums[0] < nums[1] > nums[2] < nums[3]....

You may assume the input array always has a valid answer.

Successfully Submitted
Created on Mon May 17 17:39:18 2021

@author: Christopher Obuchere
"""

from typing import List
from itertools import chain
from itertools import zip_longest
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.list_len = len(nums)
        
        self.up = 5*(10**4)
        self.down = 1
        
        self.up_n = (5**4)
        self.down_n = 0
        
#        if ( (self.list_len >= self.down) & (self.list_len <= self.up) & 
 #           all(k <= self.up_n for k in nums) & all(k >= self.down_n for k in nums)):   
        nums[:] = sorted(nums)
        mid_x = len(nums)

        if (int(mid_x%2) == 0):
            sec_1 = nums[0:int(mid_x/2)][::-1]
            sec_2 = nums[int(mid_x/2):][::-1]
        else:
            sec_1 = nums[0:int(mid_x/2)+1]
            sec_2 = nums[int(mid_x/2)+1:]

        if (len(sec_1) == len(sec_2)):
            nums[:] = list(chain.from_iterable([list(x) for x in (zip(sec_1, sec_2))]))
        else:
            nums[:] = [x for x in list(chain.from_iterable([list(x) for x in (zip_longest(sec_1, sec_2))])) if x!= None]
            
            
k = Solution()
k.wiggleSort(nums = [1,5,1,1,6,4])
