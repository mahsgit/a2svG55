class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        ans=0
        count=Counter() 
        for r in range(len(s)):
            count[s[r]]+=1
            print(count)

            while max(count.values())+k<r-l+1:
                print("count")
                count[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans
            
       
            
                