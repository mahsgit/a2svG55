class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        path=[]
        def helper(i):
            if len(path)==k:
                ans.append(path[::])
                return 

            for j in range(i+1,n+1):
                path.append(j)
                helper(j)
                path.pop()




        helper(0)
        return ans

    