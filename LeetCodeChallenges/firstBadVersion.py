# -*- coding: utf-8 -*-
"""
278. First Bad Version

You are a product manager and currently leading a team to develop a 
new product. Unfortunately, the latest version of your product fails 
the quality check. Since each version is developed based on the 
previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the 
first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether 
version is bad. Implement a function to find the first bad version. 
You should minimize the number of calls to the API.


Submitted Successfully
Created on Tue May 18 11:06:30 2021

@author: Christopher Obuchere
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        i = 1
        j = n
        
        while (i<j):
            mid_val = i + (j-i)//2
            if isBadVersion(mid_val) is False:
                i = mid_val+1
            else:
                j = mid_val
        return i