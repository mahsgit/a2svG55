class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        n=(num-3)//3
        out=[]
        if  (num-3)%3==0:
            out.append(n)
            out.append(n+1)
            out.append(n+2)
            return out
        else:
           return []





        