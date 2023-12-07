class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        current=0
        for i in nums:
            if i==1:
                count+=i
                current= max(count,current)
            else:
                count=0
        # current= max(count,current)
        return current
    

       

                    
                
        