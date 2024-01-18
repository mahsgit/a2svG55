class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref=[0]
        
        for i in range(len(nums)):
            pref.append(pref[-1]+nums[i])
        count=Counter()
        summ=0
        for r in pref:
            summ+=count[r]
            count[r+k]+=1
        return summ

        
        




      
            
           






        