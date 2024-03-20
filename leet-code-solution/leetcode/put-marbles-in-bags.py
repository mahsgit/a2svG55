class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        values=[]
        prev=weights[0]
        for val in weights[1:]:
            prev+=val
            values.append(prev)
            prev=val
        values.sort()
        leng=len(weights)-k

        return sum(values[leng:])-sum(values[:k-1])



        