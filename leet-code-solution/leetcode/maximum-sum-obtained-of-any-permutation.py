class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        requests.sort(key=lambda x: x[1])
        maxi=requests[-1][-1]
        new=[0]*(maxi+1)
        for l,r in requests:
            new[l]+=1
            if r<len(new)-1:
               new[r+1]-=1
        pref=[0]
        for val in new:
            pref.append(pref[-1]+val)
        pref.sort(reverse=True)
        nums.sort(reverse=True)
        summ=0
        for n,p in zip(nums,pref):
            summ+=n*p
    
        return summ% (10**9 + 7)
