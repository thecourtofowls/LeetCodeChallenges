# -*- coding: utf-8 -*-
"""
273. Integer to English Words

Constraints
0 <= num <= (2**31)-1


Created on Sat Feb 27 16:49:53 2021

Submitted Successfully
@author: Christopher Obuchere
"""

class Solution:
    def numberToWords(self, num: int) -> str:
        self.num = num
        self.string_list = [int(x) for x in str(self.num)]
        self.list_1 = []
        self.up = (2**31)-1
        table_ref = {
            1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
            9: 'Nine', 10 : 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 
            70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 0: 'Zero', 11: 'Eleven', 12: 'Twelve', 
            13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen',
            18: 'Eighteen', 19: 'Nineteen'
        }
        
        if ((self.num <= self.up) & (self.num >= 0) ):
            for x in range(1,len(self.string_list)+1):
                if (-x == -1):
                    if ((self.string_list[-x] >= 0) & (int(self.string_list[-x]//10) == 0) & (len(self.string_list) == 1)):
                        a = self.string_list[-x]
                        b = table_ref.get(a)
                        self.list_1.insert(-x,b)
                    elif ((self.string_list[-x] > 0) & (int(self.string_list[-x]//10) == 0) & (len(self.string_list) > 1) & 
                          (self.string_list[-x-1] == 0)):
                        a = self.string_list[-x]
                        b = table_ref.get(a)
                        self.list_1.insert(-x,b)
                elif ((-x == -2) & (((self.string_list[-x]*10)// 10) != 0)):
                    if ((self.string_list[-x+1] == 0)):
                        a = int(str(self.string_list[-x]) + str(0))
                        b = table_ref.get(a)
                        self.list_1.insert(-x,b)
                    elif ((self.string_list[-x+1] != 0) & (self.string_list[-x] == 1)):
                        a = int(str(self.string_list[-x]) + str(self.string_list[-x+1]))
                        b = table_ref.get(a)
                        self.list_1.insert(-x, b)
                    elif ((self.string_list[-x+1] != 0) & (self.string_list[-x] != 1)):
                        a = int(str(self.string_list[-x]) + str(0))
                        b = table_ref.get(a)
                        c = int(self.string_list[-x+1])
                        d = table_ref.get(c)
                        self.list_1.insert(-x, b+' '+d)
                elif ((-x == -3) & (((self.string_list[-x]*100)// 100) != 0) ):
                    a = self.string_list[-x]
                    b = table_ref.get(a)
                    self.list_1.insert(-x,b + ' '+ 'Hundred')                    
                elif (-x == -4):
                    if ((self.string_list[-x] >= 0) & (int(self.string_list[-x]//10) == 0) & (len(self.string_list) == 4)):
                        a = self.string_list[-x]
                        b = table_ref.get(a)
                        self.list_1.insert(-x,b + ' ' + 'Thousand')
                    elif ((self.string_list[-x] > 0) & (int(self.string_list[-x]//10) == 0) & (len(self.string_list) > 1) & 
                          (self.string_list[-x-1] == 0)):
                        a = self.string_list[-x]
                        b = table_ref.get(a)
                        self.list_1.insert(-x,b+ ' ' + 'Thousand')
                elif ((-x == -5) & (((self.string_list[-x]*10)// 10) != 0)):
                    if ((self.string_list[-x+1] == 0)):
                        a = int(str(self.string_list[-x]) + str(0))
                        b = table_ref.get(a)
                        self.list_1.insert(-x,b + ' ' + 'Thousand')
                    elif ((self.string_list[-x+1] != 0) & (self.string_list[-x] == 1)):
                        a = int(str(self.string_list[-x]) + str(self.string_list[-x+1]))
                        b = table_ref.get(a)
                        self.list_1.insert(-x, b + ' ' + 'Thousand')
                    elif ((self.string_list[-x+1] != 0) & (self.string_list[-x] != 1)):
                        a = int(str(self.string_list[-x]) + str(0))
                        b = table_ref.get(a)
                        c = int(self.string_list[-x+1])
                        d = table_ref.get(c)
                        self.list_1.insert(-x, b+' '+d + ' ' + 'Thousand')
                elif ((-x == -6) & (((self.string_list[-x]*100)// 100) != 0) ):
                    if ((self.string_list[-x+1] == 0) & (self.string_list[-x+2] == 0)):
                        a = self.string_list[-x]
                        b = table_ref.get(a)
                        self.list_1.insert(-x,b + ' '+ 'Hundred Thousand')
                    else:                     
                        a = self.string_list[-x]
                        b = table_ref.get(a)
                        self.list_1.insert(-x,b + ' '+ 'Hundred')                    
                elif (-x == -7):
                    if ((self.string_list[-x] >= 0) & (int(self.string_list[-x]//10) == 0) & (len(self.string_list) == 7)):
                        a = self.string_list[-x]
                        b = table_ref.get(a)
                        self.list_1.insert(-x,b + ' ' + 'Million')
                    elif ((self.string_list[-x] > 0) & (int(self.string_list[-x]//10) == 0) & (len(self.string_list) > 1) & 
                          (self.string_list[-x-1] == 0)):
                        a = self.string_list[-x]
                        b = table_ref.get(a)
                        self.list_1.insert(-x,b+ ' ' + 'Million')
                elif ((-x == -8) & (((self.string_list[-x]*10)// 10) != 0)):
                    if ((self.string_list[-x+1] == 0)):
                        a = int(str(self.string_list[-x]) + str(0))
                        b = table_ref.get(a)
                        self.list_1.insert(-x,b + ' ' + 'Million')
                    elif ((self.string_list[-x+1] != 0) & (self.string_list[-x] == 1)):
                        a = int(str(self.string_list[-x]) + str(self.string_list[-x+1]))
                        b = table_ref.get(a)
                        self.list_1.insert(-x, b + ' ' + 'Million')
                    elif ((self.string_list[-x+1] != 0) & (self.string_list[-x] != 1)):
                        a = int(str(self.string_list[-x]) + str(0))
                        b = table_ref.get(a)
                        c = int(self.string_list[-x+1])
                        d = table_ref.get(c)
                        self.list_1.insert(-x, b+' '+d + ' ' + 'Million')
                elif ((-x == -9) & (((self.string_list[-x]*100)// 100) != 0) ):
                    if ((self.string_list[-x+1] == 0) & (self.string_list[-x+2] == 0)):
                        a = self.string_list[-x]
                        b = table_ref.get(a)
                        self.list_1.insert(-x,b + ' '+ 'Hundred Million')
                    else:
                        a = self.string_list[-x]
                        b = table_ref.get(a)
                        self.list_1.insert(-x,b + ' '+ 'Hundred')
                    
                elif (-x == -10):
                    if ((self.string_list[-x] >= 0) & (int(self.string_list[-x]//10) == 0) & (len(self.string_list) == 10)):
                        a = self.string_list[-x]
                        b = table_ref.get(a)
                        self.list_1.insert(-x,b + ' ' + 'Billion')
                    elif ((self.string_list[-x] > 0) & (int(self.string_list[-x]//10) == 0) & (len(self.string_list) > 1) & 
                          (self.string_list[-x-1] == 0)):
                        a = self.string_list[-x]
                        b = table_ref.get(a)
                        self.list_1.insert(-x,b+ ' ' + 'Billion')
        
            return ' '.join(self.list_1)
        else:
                print("Constraints Not Met:\n\t 1. 0 <= num <= (2**31)-1")
                                        

k = Solution()
k.numberToWords(num = 10010010000)


k.numberToWords(num = 123)

k.numberToWords(num = 1234567891)
