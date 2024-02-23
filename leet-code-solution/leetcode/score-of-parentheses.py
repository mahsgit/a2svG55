class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0]
        for i  in range(len(s)):
            if  s[i]=='(':
                stack.append(0)
            else:
                val=stack.pop()
                k=max(1,2*val)
                n=stack.pop()
                stack.append(k+n)

    
        return stack[-1]
        
        