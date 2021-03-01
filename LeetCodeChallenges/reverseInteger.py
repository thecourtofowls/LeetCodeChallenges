# -*- coding: utf-8 -*-
"""
7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range 
[-(2**31), (2**31) - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers 
(signed or unsigned).

Constraints:

-(2**31) <= x <= (2**31) - 1

Submitted Successfully
Created on Mon Mar  1 12:20:20 2021

@author: Christopher Obuchere
"""

class Solution:
    def reverse(self, x: int) -> int:
        self.num = x
        self.string_list = [x for x in str(self.num)]
        self.list_1 = []
        self.up = (2**31)-1
        self.down = -(2**31)
                
        if ((self.num <= self.up) & (self.num >= self.down) ):
            
            if (len(self.string_list) == 1):
                a = str(self.string_list[0])
                self.list_1.insert(0, a)
            
            if (len(self.string_list) == 2):
                if (self.string_list[0] == '-'):
                    a = self.string_list[0]
                    b = self.string_list[1]
                    self.list_1.insert(0, a)
                    self.list_1.insert(1, b)
                elif (self.string_list[0] != '-'):
                    a = self.string_list[0]
                    b = self.string_list[1]
                    self.list_1.insert(0, b)
                    self.list_1.insert(1, a)
            
            if (len(self.string_list) == 3):
                if (self.string_list[0] == '-'):
                    a = self.string_list[0]
                    b = self.string_list[1]
                    c = self.string_list[2]
                    self.list_1.insert(0, a)
                    self.list_1.insert(1, c)
                    self.list_1.insert(2, b)
                elif (self.string_list[0] != '-'):
                    a = self.string_list[0]
                    b = self.string_list[1]
                    c = self.string_list[2]
                    self.list_1.insert(0, c)
                    self.list_1.insert(1, b)
                    self.list_1.insert(2, a)
            
            if (len(self.string_list) == 4):
                if (self.string_list[0] == '-'):
                    a = self.string_list[0]
                    b = self.string_list[1]
                    c = self.string_list[2]
                    d = self.string_list[3]
                    self.list_1.insert(0, a)
                    self.list_1.insert(1, d)
                    self.list_1.insert(2, c)
                    self.list_1.insert(3, b)
                elif (self.string_list[0] != '-'):
                    a = self.string_list[0]
                    b = self.string_list[1]
                    c = self.string_list[2]
                    d = self.string_list[3]
                    self.list_1.insert(0, d)
                    self.list_1.insert(1, c)
                    self.list_1.insert(2, b)
                    self.list_1.insert(3, a)
                    
            if (len(self.string_list) == 5):
                if (self.string_list[0] == '-'):
                    a = self.string_list[0]
                    b = self.string_list[1]
                    c = self.string_list[2]
                    d = self.string_list[3]
                    e = self.string_list[4]
                    self.list_1.insert(0, a)
                    self.list_1.insert(1, e)
                    self.list_1.insert(2, d)
                    self.list_1.insert(3, c)
                    self.list_1.insert(4, b)
                elif (self.string_list[0] != '-'):
                    a = self.string_list[0]
                    b = self.string_list[1]
                    c = self.string_list[2]
                    d = self.string_list[3]
                    e = self.string_list[4]
                    self.list_1.insert(0, e)
                    self.list_1.insert(1, d)
                    self.list_1.insert(2, c)
                    self.list_1.insert(3, b)
                    self.list_1.insert(4, a)
                    
            if (len(self.string_list) == 6):
                if (self.string_list[0] == '-'):
                    a = self.string_list[0]
                    b = self.string_list[1]
                    c = self.string_list[2]
                    d = self.string_list[3]
                    e = self.string_list[4]
                    f = self.string_list[5]
                    self.list_1.insert(0, a)
                    self.list_1.insert(1, f)
                    self.list_1.insert(2, e)
                    self.list_1.insert(3, d)
                    self.list_1.insert(4, c)
                    self.list_1.insert(5, b)
                elif (self.string_list[0] != '-'):
                    a = self.string_list[0]
                    b = self.string_list[1]
                    c = self.string_list[2]
                    d = self.string_list[3]
                    e = self.string_list[4]
                    f = self.string_list[5]
                    self.list_1.insert(0, f)
                    self.list_1.insert(1, e)
                    self.list_1.insert(2, d)
                    self.list_1.insert(3, c)
                    self.list_1.insert(4, b)
                    self.list_1.insert(5, a)
                    
            if (len(self.string_list) == 7):
                if (self.string_list[0] == '-'):
                    a = self.string_list[0]
                    b = self.string_list[1]
                    c = self.string_list[2]
                    d = self.string_list[3]
                    e = self.string_list[4]
                    f = self.string_list[5]
                    g = self.string_list[6]
                    self.list_1.insert(0, a)
                    self.list_1.insert(1, g)
                    self.list_1.insert(2, f)
                    self.list_1.insert(3, e)
                    self.list_1.insert(4, d)
                    self.list_1.insert(5, c)
                    self.list_1.insert(6, b)
                elif (self.string_list[0] != '-'):
                    a = self.string_list[0]
                    b = self.string_list[1]
                    c = self.string_list[2]
                    d = self.string_list[3]
                    e = self.string_list[4]
                    f = self.string_list[5]
                    g = self.string_list[6]
                    self.list_1.insert(0, g)
                    self.list_1.insert(1, f)
                    self.list_1.insert(2, e)
                    self.list_1.insert(3, d)
                    self.list_1.insert(4, c)
                    self.list_1.insert(5, b)
                    self.list_1.insert(6, a)
                    
            if (len(self.string_list) == 8):
                if (self.string_list[0] == '-'):
                    a = self.string_list[0]
                    b = self.string_list[1]
                    c = self.string_list[2]
                    d = self.string_list[3]
                    e = self.string_list[4]
                    f = self.string_list[5]
                    g = self.string_list[6]
                    h = self.string_list[7]
                    self.list_1.insert(0, a)
                    self.list_1.insert(1, h)
                    self.list_1.insert(2, g)
                    self.list_1.insert(3, f)
                    self.list_1.insert(4, e)
                    self.list_1.insert(5, d)
                    self.list_1.insert(6, c)
                    self.list_1.insert(7, b)
                elif (self.string_list[0] != '-'):
                    a = self.string_list[0]
                    b = self.string_list[1]
                    c = self.string_list[2]
                    d = self.string_list[3]
                    e = self.string_list[4]
                    f = self.string_list[5]
                    g = self.string_list[6]
                    h = self.string_list[7]
                    self.list_1.insert(0, h)
                    self.list_1.insert(1, g)
                    self.list_1.insert(2, f)
                    self.list_1.insert(3, e)
                    self.list_1.insert(4, d)
                    self.list_1.insert(5, c)
                    self.list_1.insert(6, b)
                    self.list_1.insert(7, a)
                    
            if (len(self.string_list) == 9):
                if (self.string_list[0] == '-'):
                    a = self.string_list[0]
                    b = self.string_list[1]
                    c = self.string_list[2]
                    d = self.string_list[3]
                    e = self.string_list[4]
                    f = self.string_list[5]
                    g = self.string_list[6]
                    h = self.string_list[7]
                    i = self.string_list[8]
                    self.list_1.insert(0, a)
                    self.list_1.insert(1, i)
                    self.list_1.insert(2, h)
                    self.list_1.insert(3, g)
                    self.list_1.insert(4, f)
                    self.list_1.insert(5, e)
                    self.list_1.insert(6, d)
                    self.list_1.insert(7, c)
                    self.list_1.insert(8, b)
                elif (self.string_list[0] != '-'):
                    a = self.string_list[0]
                    b = self.string_list[1]
                    c = self.string_list[2]
                    d = self.string_list[3]
                    e = self.string_list[4]
                    f = self.string_list[5]
                    g = self.string_list[6]
                    h = self.string_list[7]
                    i = self.string_list[8]
                    self.list_1.insert(0, i)
                    self.list_1.insert(1, h)
                    self.list_1.insert(2, g)
                    self.list_1.insert(3, f)
                    self.list_1.insert(4, e)
                    self.list_1.insert(5, d)
                    self.list_1.insert(6, c)
                    self.list_1.insert(7, b)
                    self.list_1.insert(8, a)
                    
            if (len(self.string_list) == 10):
                if (self.string_list[0] == '-'):
                    a = self.string_list[0]
                    b = self.string_list[1]
                    c = self.string_list[2]
                    d = self.string_list[3]
                    e = self.string_list[4]
                    f = self.string_list[5]
                    g = self.string_list[6]
                    h = self.string_list[7]
                    i = self.string_list[8]
                    j = self.string_list[9]
                    self.list_1.insert(0, a)
                    self.list_1.insert(1, j)
                    self.list_1.insert(2, i)
                    self.list_1.insert(3, h)
                    self.list_1.insert(4, g)
                    self.list_1.insert(5, f)
                    self.list_1.insert(6, e)
                    self.list_1.insert(7, d)
                    self.list_1.insert(8, c)
                    self.list_1.insert(9, b)
                elif (self.string_list[0] != '-'):
                    a = self.string_list[0]
                    b = self.string_list[1]
                    c = self.string_list[2]
                    d = self.string_list[3]
                    e = self.string_list[4]
                    f = self.string_list[5]
                    g = self.string_list[6]
                    h = self.string_list[7]
                    i = self.string_list[8]
                    j = self.string_list[9]
                    self.list_1.insert(0, j)
                    self.list_1.insert(1, i)
                    self.list_1.insert(2, h)
                    self.list_1.insert(3, g)
                    self.list_1.insert(4, f)
                    self.list_1.insert(5, e)
                    self.list_1.insert(6, d)
                    self.list_1.insert(7, c)
                    self.list_1.insert(8, b)
                    self.list_1.insert(9, a)
                    
            if (len(self.string_list) == 11):
                if (self.string_list[0] == '-'):
                    a = self.string_list[0]
                    b = self.string_list[1]
                    c = self.string_list[2]
                    d = self.string_list[3]
                    e = self.string_list[4]
                    f = self.string_list[5]
                    g = self.string_list[6]
                    h = self.string_list[7]
                    i = self.string_list[8]
                    j = self.string_list[9]
                    k = self.string_list[10]
                    self.list_1.insert(0, a)
                    self.list_1.insert(1, k)
                    self.list_1.insert(2, j)
                    self.list_1.insert(3, i)
                    self.list_1.insert(4, h)
                    self.list_1.insert(5, g)
                    self.list_1.insert(6, f)
                    self.list_1.insert(7, e)
                    self.list_1.insert(8, d)
                    self.list_1.insert(9, c)
                    self.list_1.insert(10, b)
                else:
                     return 0
            
            integer_val = int(''.join(self.list_1))
            test = lambda integer_val: integer_val if (integer_val <= self.up and integer_val >= self.down) else 0
            return test(integer_val)
        else:
            return 0
        
k = Solution()
k.reverse(x = 47)

