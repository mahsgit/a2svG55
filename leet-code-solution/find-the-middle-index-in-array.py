class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix=[0]

        for n in range(1,len(nums)+1 ):
            prefix.append(prefix[-1]+nums[n-1])
        prefix.extend([prefix[-1]])
        for i in range(len(nums)):
            if prefix[i]==prefix[-1]-prefix[i+1]:
                return i
        return -1
        