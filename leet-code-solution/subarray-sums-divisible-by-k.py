class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref=[0]
        rem=[]
        count=Counter()
        ans=0
        for i in nums:
            pref.append(pref[-1]+i)
        for i in pref:
            rem.append(i%k)
        for i in rem:
            ans+=count[i]
            count[i]+=1
        return ans


   