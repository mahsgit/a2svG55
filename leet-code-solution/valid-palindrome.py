class Solution:
    def isPalindrome(self, s: str) -> bool:
        
       clean_string = ''.join(c for c in s if c.isalnum())
       i=0
       j=len(clean_string)-1
       clean_string=clean_string.lower()
       while i<=j:
           if clean_string[i]!=clean_string[j]:
               return False
           i+=1
           j-=1
       return True