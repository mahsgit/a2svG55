class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def helper(k,n):
            if n==0:
                return False
            elif k>(2**n)//2:
                return not helper(k-((2**n)//2),n-1)
            else:
                return helper(k,n-1)
        

        return  1 if helper(k,n) else 0
        