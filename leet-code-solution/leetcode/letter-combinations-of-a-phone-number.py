class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans=[]
        path=[]
        mapp={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        k=len(digits)


        def helper(l):

            if len(path)==k:
                ans.append("".join(path[::]))
                return 

            if len(path) >k:
                return 

            for j in mapp[digits[l]]:
                path.append(j)
                helper(l+1)
                path.pop()



          
        if k==0:
            return []
        else:
           helper(0)
           return  ans
