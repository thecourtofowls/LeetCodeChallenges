# -*- coding: utf-8 -*-
"""
80. Remove Duplicates from Sorted Array II

Given a sorted array nums, remove the duplicates in-place such that duplicates 
appeared at most twice and return the new length.

Do not allocate extra space for another array; you must do this by modifying 
the input array in-place with O(1) extra memory.

Clarification:
Confused why the returned value is an integer, but your answer is an array?

Note that the input array is passed in by reference, which means a 
modification to the input array will be known to the caller.

Constraints:

1 <= nums.length <= 3 * (10**4)
-(10**4) <= nums[i] <= (10**4)
nums is sorted in ascending order.

Submitted Successfully
Created on Tue May 25 17:08:14 2021

@author: Christopher Obuchere
"""

import itertools
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        b = [] #Empty list
        #Get a combination of nums element and count, with replacing above 3 count with 2
        nums[:] = [[[x], nums.count(x) if nums.count(x) < 3 else 2] for x in nums]
        #Get uniquesof nested lists
        [b.append(item) for item in nums if item not in b]
        #Multiply unique and count
        a = [a[0]*a[1] for a in b]
        #Unnest list inplace
        nums[:] = list(itertools.chain(*a))
        #Get len of list
        self.len_nums = len(nums)

        return self.len_nums
    
k = Solution()
k.removeDuplicates(nums = [0,0,1,1,1,1,2,3,3])
#Output: 7, nums = [0,0,1,1,2,3,3]