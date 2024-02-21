class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        curr=list(palindrome)
        n=len(palindrome)
        if n==1:
            return  ""
        
        if n%2!=0:
            k=(n+1)//2
            k-=1
            for i,c in enumerate(curr):
                if i==k:
                    continue
                if c!='a':
                    curr[i]='a'
                    break
                
        
        elif n%2==0:
             for i,c in enumerate(curr):
                if c!='a':
                    curr[i]='a'
                    break
       
        new="".join(map(str,curr))

        if new==palindrome:
            curr[-1]='b'
            new="".join(map(str,curr))
        
        return new



        