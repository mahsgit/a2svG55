class Solution:
    def myPow(self, x: float, n: int) -> float:
      def helper(n):
          if n==1:return x
          if n==0 : return 1
          if x==0: return 0


          ans=helper(n//2)
          return ans*ans if n%2==0 else x*ans*ans


      res=helper(abs(n))
      return res if n>0 else 1/res
     
