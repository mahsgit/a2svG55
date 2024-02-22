class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
       
        
        stack=[]
        close={'}',']',')'}
        mapp={'}':'{',']':'[',')':'('}

        for i in s:
            if i not in close:
                 stack.append(i)
            else:
                if stack and  stack[-1]==mapp[i]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
             return True







