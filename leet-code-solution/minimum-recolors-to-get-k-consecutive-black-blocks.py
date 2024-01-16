class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        first=Counter(blocks[0:k])
        ans=first['W']
      
      
        for r in range(k,len(blocks)):
            first[blocks[r]]+=1
            first[blocks[r-k]]-=1
            count=first['W']
            ans=min(count,ans)
            
        return ans


        