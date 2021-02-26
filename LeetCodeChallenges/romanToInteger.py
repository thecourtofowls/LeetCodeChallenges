# -*- coding: utf-8 -*-
"""
13. Roman to Integer

Given a roman numeral, convert it to an integer.

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].


Created on Fri Feb 26 18:47:08 2021

Sucessfully Submitted

@author: Christopher Obuchere
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        string_full = s
        len_data = len(s)
        self.solution = [x for x in s]
        self._another_solution = []
        table_ref = {
            'I':'1', 'V':'5','X':'10','L':'50',
            'C':'100','D':'500','M':'1000'
        }
        
        if ((len_data <= 15) & (len_data >= 1) & ( ('I' in s) | ('V' in s) | ('X' in s) | ('L' in s) | 
            ('C' in s) | ('D' in s) | ('M' in s) )):
            a = [table_ref.get(n, n) for n in self.solution]
            #print(a)
            if (len_data == 1):
                for rom,num in table_ref.items():
                    string_full = string_full.replace(rom,num)
                return int(string_full)
            
            elif (len_data == 2):
                for x in range(1,(len(a))):
                    if (int(a[x-1]) == int(a[x])):
                        return (int(a[x-1]) + int(a[x]))
                    elif (int(a[x-1]) < int(a[x])):
                        return (int(a[x]) - int(a[x-1]))
                    elif (int(a[x-1]) > int(a[x])):
                        return (int(a[x]) + int(a[x-1]))
                        
            elif (len_data > 2):
                for x in range(len(a)-1):
                    #print(x)
                    if (int(a[x]) > int(a[x+1])):
                        self._another_solution.append(int(a[x]))
                    elif (int(a[x]) < int(a[x+1]) ):
                        self._another_solution.append(-int(a[x]))
                    elif ( int(a[x]) == int(a[x+1])):
                        self._another_solution.append(int(a[x]))
                self._another_solution.append(int(a[-1]))
                #print(self._another_solution)

            return sum(self._another_solution)
        
    
k = Solution()
k.romanToInt(s = 'ML')
