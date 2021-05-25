# -*- coding: utf-8 -*-
"""
26. Remove Duplicates from Sorted Array
Given a sorted array nums, remove the duplicates in-place such that each 
element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying 
the input array in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a 
modification to the input array will be known to the caller as well.

Constraints:

0 <= nums.length <= 3 * (10**4)
-(10**4) <= nums[i] <= (10**4)
nums is sorted in ascending order.

Submitted Successfully
Created on Thu May 20 15:26:12 2021

@author: Christopher Obuchere
"""
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = set(nums)
        nums.sort()
        return len(nums)
    
k = Solution()
k.removeDuplicates(nums = [1,1,2,3,5,5,5,6,7,7,8,9,10])