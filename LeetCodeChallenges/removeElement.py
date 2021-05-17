# -*- coding: utf-8 -*-
"""
27. Remove Element

Given an array nums and a value val, remove all instances of that value in-place and 
return the new length.

Do not allocate extra space for another array, you must do this by modifying the 
input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond 
the new length.

Submitted Successfully
Created on Mon May 17 13:06:58 2021

@author: Christopher Obuchere
"""

from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        self.list = nums
        self.list_len = len(self.list)
        self.val_rep = val
        
        self.up = (10**2)
        self.down = 0
        self.up_num = 50
        
        if ( (self.list_len >= self.down) & (self.list_len <= self.up) & (self.val_rep >= self.down) & 
            (self.val_rep <= self.up) & all(k <= self.up_num for k in self.list) & all(k >= self.down for k in self.list)):

            nums[:] =  [x for x in nums if x!= val]
            self.s_length_list = len(nums)

        return self.s_length_list
    
k = Solution()
k.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)
