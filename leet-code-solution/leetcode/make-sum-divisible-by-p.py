class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefix_sum = [0]
        ans = len(nums)
        
        countee = Counter()
        if sum(nums)%p==0:
            return 0
        
        for i in nums:
            prefix_sum.append(prefix_sum[-1] + i)

        v = prefix_sum[-1] % p
        modu = []

        for i in prefix_sum:
            modu.append((i + v) % p)
            
        for i, val in enumerate(modu):
            if (val - v) % p in countee:
                ans = min(ans, i - countee[(val - v) % p])
            countee[val] = i
        
        if ans == len(nums):
            ans = -1
        
        return ans


        