class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        x=float("inf")
        y=float("inf")

        for i in nums:
            if  i<= x:
                x=i
            elif i <= y:
                y=i
            else:
                return True


     

            
      
        
        