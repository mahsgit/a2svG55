class Solution:
    def countGoodNumbers(self, n: int) -> int:

        def helper(a, n):
            if n==0:
                return 1

            if  n%2==0 :
                return helper(a*a %( 10**9 + 7), (n)//2)  
            else :
               return a * helper(a, n-1)

        # print(helper(3, 4))
    
        return (helper(5, n - (n//2)) * helper(4, n//2))% (10**9 + 7)
        
        