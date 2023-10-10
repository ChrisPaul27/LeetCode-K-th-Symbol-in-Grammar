#The idea is that given k i can calculate in a retroactive way the useful digit ad each step
#For example, given n = 5 and k = 13, the situation is as follows:
# 0, n = 1
# 01, n = 2
# 01 10, n = 3
# 01 10 10 01, n = 4
# 01 10 10 01 10 01 01 10, n = 5
#The 13-th character of the string belonging to n = 5 could be obtained from the round(13/2)-th character, that is 7-th character, of the string belonging to n = 4. 
#This latter could be obtained from the round(7/2)-th character, that is the 4-th character of the string belonging to n = 3. 
#I repeat these steps in the first for, so that I can obtain the position needed at each step. The second for is straightforward. 

import math
class Solution(object):
    def kthGrammar(self, n, k):
        if n == 1:
            return 0
        else:
            tmp = "0"
            t = k
            pos_each_n = [None] * (n-1)
            pos_each_n[n-2] = round(float(k)/float(2)) 
            for i in range(1, n-1):
                pos_each_n[n-2-i] = round(float(pos_each_n[n-2-(i-1)])/float(2))  
            
            for i in range(1, n):
                p = 1 if pos_each_n[i-1] % 2 == 0 else 0
                if tmp[p] == "0":
                    tmp = "01"
                else:
                    tmp = "10"
            
        return int(tmp[1 if k % 2 == 0 else 0])
