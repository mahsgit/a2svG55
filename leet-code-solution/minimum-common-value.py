class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1=set(nums1)
        nums2=set(nums2)
        ans=float('inf')
        for i in nums2:
            if i in nums1 :
                ans=min(ans,i)
        if ans==float('inf'):
            return -1
        else: 
         return ans

        