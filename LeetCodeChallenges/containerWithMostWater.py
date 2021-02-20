# -*- coding: utf-8 -*-
"""
11. Container With Most Water
Given n non-negative integers a1, a2, ..., an , where each represents a point at 
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the 
line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis 
forms a container, such that the container contains the most water.


Time Limit Exceeeded
Created on Sat Feb 20 17:19:03 2021

@author: BACH
"""

height = [1,1]#1
height = [4,3,2,1,4]#16
height = [1,2,1]#2

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        self.height = height
        self._data_len = len(height)
        self.base = 0
        self.solution = []
        self.range = range(self._data_len)
        self.max = 0
        self.up = 3*(10**4)

        if ((self._data_len >= 2) & (self._data_len <= self.up) & all(k <= self.up for k in self.height) & 
            all(k >= self.base for k in self.height)):
            for self.i in self.range:
                for x in self.range:
                    if ((self.i >= self.base) & (self.height[self.i] <= self.height[x]) & 
                        (((self.height[self.i]-self.base) * abs(self.i-x)) > self.max) ):
                            self.max = (self.height[self.i]-self.base) * abs(self.i-x)
            return self.max
#
k = Solution()
k.maxArea(height = height)

"""
T0 Do: Optimize Further

#46 / 56 test cases passed.
"""
