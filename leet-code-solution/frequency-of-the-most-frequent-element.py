class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l=0
        ans=0
        nums.sort()
        size=len(nums)
        # maxi=1
        # for s in range(2,size+1):
        #     check=sum(nums[:s])
        #     if nums[s-1]*s-check<=k:
        #         maxi=max(maxi,s)
        #     for i in range(s,size):
        #         check+=nums[i]
        #         check-=nums[i-s]
        #         if nums[i]*s-check<=k:
        #            maxi=max(maxi,s)

        # return maxi


        check=nums[0]
        l=0
        maxi=1
        for r in range(1,len(nums)):
            check+=nums[r]
            while nums[r]*(r-l+1) - check>k:
                check-=nums[l]
                l+=1
            maxi=max(r-l+1,maxi)
        return maxi



            




            

            


      


        