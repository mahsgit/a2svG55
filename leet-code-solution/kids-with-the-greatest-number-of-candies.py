class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out=[]
        for i in candies:
            new=i+extraCandies
            if new>=max(candies):
                out.append(True)
            else:
                out.append(False)
        return out
        