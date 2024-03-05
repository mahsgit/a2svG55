class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]
        n=len(nums)

        def helper(i):
            if len(path)==n:
                res.append(path[:])
                return
            
            for j in range(n):
                if nums[j] not in path:
                    path.append(nums[j])
                    helper(j)
                    path.pop()
          




        helper(0)
        return res
        