class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        ans=0
        count=0
        if len(piles)==3:
            return piles[1]
        for i in  range(1,len(piles)-2,2):
            ans+=piles[i]
            count+=1
            if count==len(piles)//3:
                break
        return ans

        