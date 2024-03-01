class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def helper(n):
            if n<=0 :
                return False
            if n==1:
                return True

            return helper(n/3)
            
        return helper(n)
        