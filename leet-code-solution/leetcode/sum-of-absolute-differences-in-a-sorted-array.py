class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pref=[nums[0]]
        n=len(nums)

        for i in range(1,len(nums)):
            pref.append(pref[-1]+nums[i])

        ans=[pref[-1]-nums[0]*n]
        

        for i in  range(1,n):
            ans.append( ((nums[i]*(i+1))-pref[i]) +  (pref[-1]-pref[i]-nums[i]*(n-i-1)) )
        return ans


        