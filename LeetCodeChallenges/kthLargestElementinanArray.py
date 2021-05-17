# -*- coding: utf-8 -*-
"""
215. Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element 
in the array.

Note that it is the kth largest element in the sorted order, not the kth 
distinct element.

Constraints:

1 <= k <= nums.length <= 10**4
-(10**4) <= nums[i] <= 10**4

Submitted Successfully
Created on Mon May 17 17:23:36 2021

@author: Christopher Obuchere
"""

from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        self.list_len = len(nums)
        
        self.up = (10**4)
        self.down = 1
        
        self.up_n = (10**4)
        self.down_n = -(10**4)
        
        if ( (self.list_len >= self.down) & (self.list_len <= self.up) & 
            (k >= self.down) & (k <= self.up) &
            all(k <= self.up_n for k in nums) & all(k >= self.down_n for k in nums)):
            
            k_max = sorted(nums)[len(nums)-k]

            return k_max
        
k = Solution()
k.findKthLargest(nums = [3,2,1,5,6,4], k = 2)