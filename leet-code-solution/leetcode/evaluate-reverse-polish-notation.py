class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for val in tokens:
            if val=='+':
                a=stack.pop()
                b=stack.pop()
                stack.append(b+a)


            elif val=='-':
                a=stack.pop()
                b=stack.pop()
                stack.append(b-a)


            elif val=='*':
                a=stack.pop()
                b=stack.pop()
                stack.append(b*a)


            elif val=='/':
                a=stack.pop()
                b=stack.pop()
                divi=b/a
                if divi<=0:
                   stack.append(ceil(divi))
                else:
                    stack.append(floor(divi))



            else:
                stack.append(int(val))

                
        return stack[-1]
      