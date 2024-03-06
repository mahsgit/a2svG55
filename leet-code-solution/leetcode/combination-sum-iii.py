class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        path=[]
        def helper(i,tar):

            if tar==0 and len(path)==k:
                ans.append(path[:])
                return
            if len(path)>k:
                return
            for j in range(i+1,10):
                path.append(j)
                helper(j,tar-j)
                path.pop()


        helper(0 ,n)
        return ans
        