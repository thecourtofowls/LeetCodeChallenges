# -*- coding: utf-8 -*-
"""
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the 
index if the target is found. If not, return the index where it would be if 
it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Constraints:

1 <= nums.length <= (10**4)
-(10**4) <= nums[i] <= (10**4)
nums contains distinct values sorted in ascending order.
-(10**4) <= target <= (10**4)

Submitted Successfully
Created on Tue May 18 10:47:53 2021

@author: Christopher Obuchere
"""

from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        self.list_len = len(nums)
        
        set_list = set(nums)
        set_len = len(set_list)
        
        self.up = (10**4)
        self.down = 1
        self.down_t = -(10**4)
                
        if ( (self.list_len >= self.down) & (self.list_len <= self.up) & 
            (target >= self.down_t) & (target <= self.up) & (set_len == self.list_len) & #Check uniqueness
            all(k <= self.up for k in nums) & all(k >= self.down_t for k in nums)):
            
            try:
                index_target = nums.index(target)
            except ValueError:
                nums[:] = nums+[target]
                index_target = sorted(nums).index(target)

            return index_target

k = Solution()
k.searchInsert(nums = [1,3,5,6], target = 2)
