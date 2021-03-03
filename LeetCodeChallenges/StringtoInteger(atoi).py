# -*- coding: utf-8 -*-
"""
8. String to Integer (atoi)

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer 
(similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is '-' or '+'. 
    Read this character in if it is either. This determines if the final result is 
    negative or positive respectively. Assume the result is positive if neither is present.
3. Read in next the characters until the next non-digit charcter or the end of the input 
    is reached. The rest of the string is ignored.
4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits 
    were read, then the integer is 0. Change the sign as necessary (from step 2).
5. If the integer is out of the 32-bit signed integer range [-(2**31), (2**31) - 1], then clamp 
    the integer so that it remains in the range. Specifically, integers less than -231 
    should be clamped to -(2**31), and integers greater than (2**31) - 1 should be clamped to 231 - 1.
6. Return the integer as the final result.
Note:

+ Only the space character ' ' is considered a whitespace character.
+ Do not ignore any characters other than the leading whitespace or the rest of the string after
     the digits.

Constraints:
+ 0 <= s.length <= 200
+ s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.


Submitted successfully
Created on Wed Mar  3 15:40:19 2021

@author: Christopher Obuchere
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        self.string = s
        self.s_length = len(s)
        self.string_no_lead_ws = self.string.lstrip()
        self.string_list = [int(x) if x.isdigit() else x.lstrip() for x in self.string_no_lead_ws]
        self.list_1 = []
        self.up = 200
        self.down = 0
        self.up_range = (2**31)-1
        self.down_range = -(2**31)
                
        if ((self.s_length <= self.up) & (self.s_length >= self.down) & (len(self.string_list) > 0)):
            
            if (self.s_length == 0):
                return 0
            
            elif ((self.s_length == 1) & 
                  ((self.string_list[0] == '-') or (self.string_list[0] == '+') or (self.string_list[0] == ' ') or 
                   (self.string_list[0] == '.') or (type(self.string_list[0]) != int) or (self.string_list[0] == '') )):
                return 0
            
            elif ((self.s_length == 1) and (type(self.string_list[0]) == int)):
                self.list_1.insert(0, self.string_list[0])      
            
            elif ((self.string_list[0] == '-') and (self.s_length > 1) and (type(self.string_list[1]) == int) ):
                self.list_1.insert(0, '-')
                for x in range(1, len(self.string_list)):
                    if ((type(self.string_list[x]) == int) ):
                        self.list_1.append(self.string_list[x])
                    elif ( (self.string_list[x] == '-') and ((self.string_list[x] == '+') or (self.string_list[x] == '-') )):
                        break
                    elif ( (self.string_list[x] == '+') and ((self.string_list[x] == '+') or (self.string_list[x] == '-') )):
                        break
                    elif ((self.string_list[x] == '+') or (self.string_list[x] == '-')):
                        return 0      
                    else:
                        break
            
            elif ((self.string_list[0] == '+') and (self.s_length > 1) and (type(self.string_list[1]) == int)):
                self.list_1.insert(0, '+')
                for x in range(1, len(self.string_list)):
                    if ((type(self.string_list[x]) == int) ):
                        self.list_1.append(self.string_list[x])
                    elif ((self.string_list[x] == '+') or (self.string_list[x] == '-')):
                        return 0
                    else:
                        break
                        
            elif ((type(self.string_list[0]) == int) and (self.s_length > 1)):
                for x in range(0, len(self.string_list)):
                    if ((type(self.string_list[x]) == int) ):
                        self.list_1.append(self.string_list[x])                        
                    else:
                        break
           
            else:
                return 0
        else:
                return 0
        
        integer_val = int(''.join([str(x).rstrip() for x in self.list_1]))
        test = lambda x: x if ((x <= self.up_range) & (x >= self.down_range)) else self.up_range if (x > self.up_range) else self.down_range if (x < self.down_range) else 0
        return test(integer_val)

k = Solution()
k.myAtoi(s = "-13+8")
