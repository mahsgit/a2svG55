from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures) ):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                val=stack.pop()
                res[val]=i-val
    
            stack.append(i)
     

        return res

