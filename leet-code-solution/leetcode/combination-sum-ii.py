class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

            ans=[]
            path=[]
            n=len(candidates)
            check=set()
            tar=target
            candidates.sort()
               


            def helper(l,tar):

                if tuple(path) not in check and tar==0:
                    ans.append(path[::])
                    check.add(tuple(path))

                p=-20

                for i  in range(l,n):  
                    if tar<0:
                        return 
                    if candidates[i]==p:
                         continue    
                    path.append(candidates[i])
                    helper(i+1,tar-candidates[i])
                    p=path.pop()


            helper(0,target)
            return ans
        
            