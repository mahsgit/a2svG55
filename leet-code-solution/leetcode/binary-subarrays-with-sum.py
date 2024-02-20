class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref=0
        ans=0
        dictio=defaultdict(int)
        dictio[0]+=1
        for i in range(len(nums)):
            pref+=nums[i]
            check=pref-goal
            ans+=dictio[check]
            dictio[pref]+=1
        return ans
            