# -*- coding: utf-8 -*-
"""
75. Sort Colors
Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, 
and blue, respectively.

You must solve this problem without using the library's sort function.

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2

Submitted Successfully
Created on Mon May 17 20:29:41 2021

@author: Christopher Obuchere
"""

from typing import List
class Solution:
    def sortColors(self, nums: List[int]):# -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        self.nums_len = len(nums)
        self.up = 300
        self.down = 1
        
        if ( (self.nums_len >= self.down) & (self.nums_len <= self.up) & 
            (any(k == 0 for k in nums) | any(k == 1 for k in nums) | any(k == 2 for k in nums) )):
            #nums[:] = sorted(nums) Inbuilt
            
            if (self.nums_len == 1):
                nums[:] = nums
                #return nums
            elif (self.nums_len == 2):
                if nums[0] > nums[1]:
                    nums[0],nums[1] = nums[1],nums[0]
                #return nums
            elif (self.nums_len > 2):
                j = 0
                while j <= self.nums_len:
                    for i in range(self.nums_len-1):
                        if (nums[i] >= nums[i+1]):
                            nums[i], nums[i+1] = nums[i+1],nums[i]
                    j += 1
                #return nums

#k = Solution()
#k.sortColors(nums = [2,1,0])