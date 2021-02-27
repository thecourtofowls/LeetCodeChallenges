# -*- coding: utf-8 -*-
"""
12. Integer to Roman

Constraints:

1 <= num <= 3999

Created on Sat Feb 27 12:01:28 2021

Submitted Successfully

@author: Christopher Obuchere
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        self.num = num
        self.string_list = [int(x) for x in str(self.num)]
        self.list_1 = []
        table_ref = {
            1 : 'I', 5 : 'V', 10 : 'X',50 : 'L',
            100 : 'C', 500 : 'D', 1000 : 'M'
        }
        
        if ((self.num <= 3999) & (self.num >= 1) ):
            for x in range(1,len(self.string_list)+1):
                if ((-x == -1) & (self.string_list[-x] != 0) & (self.string_list[-x]//10 == 0) ):
                    if ((self.string_list[-x] < 5) & ((5-self.string_list[-x]) > 1)):
                        m = table_ref.get(1)
                        self.list_1.insert(-x,self.string_list[-x]*m)
                    elif ((self.string_list[-x] < 5) & ((5-self.string_list[-x]) == 1)):
                        a = table_ref.get(1)
                        b = table_ref.get(5)
                        self.list_1.insert(-x, a+b)
                    elif (self.string_list[-x] == 5):
                        a = table_ref.get(5)
                        self.list_1.insert(-x, a)
                    elif ((self.string_list[-x] > 5) & ((self.string_list[-x]-5) <= 3)):
                        difference = self.string_list[-x] - 5
                        a = table_ref.get(5)
                        b = table_ref.get(1)
                        self.list_1.insert(-x, a+(b*difference))
                    elif ((self.string_list[-x] > 5) & ((self.string_list[-x]-5) == 4)):
                        difference = 5 - self.string_list[-x]
                        a = table_ref.get(10)
                        b = table_ref.get(1)
                        self.list_1.insert(-x, b+a)
                elif ((-x == -2) & (((self.string_list[-x]*10)// 10) != 0)):
                        a = (self.string_list[-x])
                        if (((self.string_list[-x]*10)// 10) == 5):
                            b = table_ref.get(50)
                            self.list_1.insert(-x,b)
                        elif ((((self.string_list[-x]*10)// 10) < 5) &  (((self.string_list[-x]*10)// 10) < 4)):
                            b = table_ref.get(10)
                            self.list_1.insert(-x, int(a)*b)
                        elif (((self.string_list[-x]*10)// 10) == 4):
                            b = table_ref.get(50)
                            c = table_ref.get(10)
                            self.list_1.insert(-x, c+b)
                        elif ((((self.string_list[-x]*10)// 10) > 5) &  (((self.string_list[-x]*10)// 10) <= 8)):
                            b = table_ref.get(50)
                            c = table_ref.get(10)
                            diff_rence = self.string_list[-x] - 5
                            self.list_1.insert(-x, b+c*diff_rence)
                        elif (((self.string_list[-x]*10)// 10) == 9):
                            b = table_ref.get(100)
                            c = table_ref.get(10)
                            self.list_1.insert(-x, c+b)
                elif ((-x == -3) & (((self.string_list[-x]*100)// 100) != 0)):
                        a = (self.string_list[-x])
                        if (((self.string_list[-x]*100)// 100) == 5):
                            b = table_ref.get(500)
                            self.list_1.insert(-x,b)
                        elif ((((self.string_list[-x]*100)// 100) < 5) &  (((self.string_list[-x]*10)// 10) < 4)):
                            b = table_ref.get(100)
                            self.list_1.insert(-x, int(a)*b)
                        elif (((self.string_list[-x]*100)// 100) == 4):
                            b = table_ref.get(500)
                            c = table_ref.get(100)
                            self.list_1.insert(-x, c+b)
                        elif ((((self.string_list[-x]*100)// 100) > 5) &  (((self.string_list[-x]*10)// 10) <= 8)):
                            b = table_ref.get(500)
                            c = table_ref.get(100)
                            diff_rence = self.string_list[-x] - 5
                            self.list_1.insert(-x, b+c*diff_rence)
                        elif (((self.string_list[-x]*100)// 100) == 9):
                            b = table_ref.get(1000)
                            c = table_ref.get(100)
                            self.list_1.insert(-x, c+b)
                elif ((-x == -4) & (((self.string_list[-x]*1000)// 1000) != 0)):
                        a = (self.string_list[-x])
                        if (((self.string_list[-x]*1000)// 1000) == 1):
                            b = table_ref.get(1000)
                            self.list_1.insert(-x, b)
                        else:
                            b = table_ref.get(1000)
                            self.list_1.insert(-x, int(a)*b)
                        
        return ''.join(self.list_1)
    
k = Solution()
k.intToRoman(num = 2989)