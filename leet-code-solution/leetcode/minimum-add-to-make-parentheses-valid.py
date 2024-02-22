class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        check=defaultdict(int)
        count=0
        for i in s:
            if i=='(':
                check['(']+=1

            elif i==')':
                if check['(']>0:
                   check['(']-=1
                else:
                    count+=1
        if check['(']<0:
           return count
        else:
            return count + check['(']


    

        