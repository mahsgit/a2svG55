class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x=16
        while x >=0:
            if 3**x <= n:
                n=n-3**x
            x-=1

        if n==0:
            return True
        else:
            return False


        
        
        
        