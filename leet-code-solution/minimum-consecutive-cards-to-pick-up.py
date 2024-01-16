class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        check=set()
        l=0
        mini=float('inf')
        for r ,val in enumerate(cards):

            while l<r and val in check:
                mini=min(mini,r-l+1)
                check.remove(cards[l])
                l+=1


            check.add(val)
        if mini==float('inf'):
            return -1
        else:
            return mini
        