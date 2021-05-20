# -*- coding: utf-8 -*-
"""
658. Find K Closest Elements

Given a sorted integer array arr, two integers k and x, return the k closest 
integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Constraints:

1 <= k <= arr.length
1 <= arr.length <= (10**4)
arr is sorted in ascending order.
-(10**4) <= arr[i], x <= (10**4)

Submitted Successfully
Created on Wed May 19 22:36:25 2021

@author: Christopher  Obuchere
"""
from typing import List
import itertools
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        self.list_len = len(arr)
        self.up = (10**4)
        self.down = 1
        self.down_x =-(10**4)
        
        if ( (self.list_len >= self.down) & (self.list_len <= self.up) & (x >= self.down_x) & (x <= self.up) & 
            all(k <= self.up for k in arr) & all(k >= self.down_x for k in arr)):
            #Conditionscheck
            
            if (self.list_len == 1):
                return arr
            elif (self.list_len > 1):
                if (k == self.list_len):
                    return arr
                elif (k != self.list_len):
                    n = [abs(arr[i]-x) for i in range(len(arr))]
                    nn = len(n)
                    m = [[arr[i:i+k],sum(n[i:i+k])] for i in range(nn-k+1) ]
                    min_m = min([x[-1] for x in m])
                    a_list = [x[:-1] for x in m if x[-1] == min_m] #provides lists nested 
                    #print(a_list)
                    if (len(a_list) == 1):
                        b_list = list(itertools.chain(*a_list)) #unnestlist
                        c_list = list(itertools.chain(*b_list))
                    else:
                        a_list[:] = a_list[0] #If list are 2, take the1st
                        c_list = list(itertools.chain(*a_list))
                    
                    return c_list
    
k = Solution()
k.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3)
