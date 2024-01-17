class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:     
        length = len(cardPoints)
        check=ans=sum(cardPoints[:k])
        for i in range(1,k+1):
            check-=cardPoints[k-i]
            check+=cardPoints[-i]

            ans=max(check,ans)
        return ans


        


        