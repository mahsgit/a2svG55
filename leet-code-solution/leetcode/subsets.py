class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        path=[]
        l=len(nums)
        def helper(i):
            ans.append(path[:])


            for j in range(i+1,l+1):
                path.append(nums[j-1])
                helper(j)
                path.pop()

           


        helper(0)
        return ans

        