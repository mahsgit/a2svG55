class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # prefix = ""
        
        # if not strs:
        #     return prefix
        
        # for i in range(len(strs[0])):
        #     ch = strs[0][i]
        #     for j in range(1, len(strs)):
        #         currentStr = strs[j]
        #         if i >= len(currentStr) or currentStr[i] != ch:
        #             return prefix
        #     prefix += ch
        
        # return prefix

        maxi=200
        j=0

        result=""
        for i in range(len(strs)):
            maxi=min(maxi,len(strs[i]))


        for i in range(maxi):
            j=0
            while j<len(strs)-1:
                if strs[j][i] == strs[j+1][i] :
                    print(strs[j][i], strs[j], strs[j+1]  )
                    j+=1
                else:
                    return result
            result+=strs[j][i]
            print(result)


        return result

                



            
        

        