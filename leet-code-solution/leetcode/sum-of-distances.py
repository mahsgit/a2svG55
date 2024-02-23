class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        count=Counter()
        mapp=defaultdict(list)
        ans=[0]*len(nums)
        for i in range(len(nums)):
            mapp[nums[i]].extend([i])
            count[nums[i]]+=1
        for key, valu in mapp.items():
            pre_sum, suf_sum = 0, sum(valu)
            p, s = 0, len(valu)
            for i in valu:
                pre_sum += i
                suf_sum -= i
                p += 1
                s -= 1
                ans[i] = -pre_sum + i*p + suf_sum - i*s

        return ans
