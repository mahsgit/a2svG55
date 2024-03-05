class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        path=[]
        n=len(nums)
        check=set()
        nums.sort()
        def helper(l):
            if tuple(path) not in check:
                ans.append(path[:])
                check.add(tuple(path))


            for j in range(l,n):
                path.append(nums[j])
                helper(j+1)
                path.pop()


         


        helper(0)
        return ans
        