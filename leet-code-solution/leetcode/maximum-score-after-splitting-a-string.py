class Solution:
    def maxScore(self, s: str) -> int:
        zero=0
        s=list(map(int,s))
        one=sum(s[1:])
        if s[0]==0:
            zero+=1
        maxi=(one+zero)
        for i in range(1,len(s)-1):
            if s[i]==0:
                zero+=1
            else:
                one-=1
            maxi=max(one+zero,maxi)
        return maxi

        
        