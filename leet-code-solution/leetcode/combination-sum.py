class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        tar=target
        path=[]
        ans=[]
        n=len(candidates)
        def helper(l,tar):
            if tar==0:
                ans.append(path[::])
            if tar<0:
                        return   

      


            for j in range(l,n):
                    

                    path.append(candidates[j])
                    helper(j,tar-candidates[j])
                    path.pop()

        helper(0,target)
        return ans
        