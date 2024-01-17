class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        new=[0]
        for i in range(len(nums)):
            new.append(new[-1]+nums[i]%2)
        summ=0

        count=Counter(new)
        for  i in new:
            summ+=count[i-k]
        return summ

     
        

         