# -*- coding: utf-8 -*-
"""
28. Implement strStr()

Return the index of the first occurrence of needle in haystack, or -1 if 
needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? 
For the purpose of this problem, we will return 0 when needle is an empty 
string. This is consistent to C's strstr() and Java's indexOf().

Constraints:

1. 0 <= haystack.length, needle.length <= 5 * 104
2. haystack and needle consist of only lower-case English characters.

Submitted Successfully

Created on Fri Mar 12 14:03:30 2021

@author: Christopher Obuchere
"""
import re
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        self.haystack = haystack
        self.needle = needle
        
        self.haystack_no_ws = self.haystack.strip() 
        self.haystack_len = len( self.haystack_no_ws)
        
        self.needle_no_ws = self.needle.strip() 
        self.needle_len = len( self.needle_no_ws)
        
        self.up_range = 5*(10**4)
        self.down_range = 0
        
        if ((self.haystack_len >= self.down_range) & (self.haystack_len <= self.up_range) & 
            (self.needle_len >= self.down_range) & (self.needle_len <= self.up_range)):
            if ((self.haystack_len == self.down_range) & (self.needle_len != self.down_range)):
                return -1
            elif ((self.haystack_len >= self.down_range) & (self.needle_len == self.down_range)):
                return 0
            elif ((self.haystack_len > self.down_range) & (self.needle_len > self.down_range)):
                result = re.search(pattern = self.needle, string = self.haystack)
                if (result == None):
                    return -1
                else:
                    return result.start()
                
k = Solution()
k.strStr(haystack = "hello", needle = "ll")#2

k = Solution()
k.strStr(haystack = "aaaaa", needle = "bba")#-1

k = Solution()
k.strStr(haystack = "", needle = "")#0

k = Solution()
k.strStr(haystack = "", needle = "a")#-1

k = Solution()
k.strStr(haystack = "a", needle = "")#0

