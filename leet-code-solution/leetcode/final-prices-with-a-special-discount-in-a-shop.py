class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        new=[0]*len(prices)
        pricess=prices
        stack=[]
        count=0
        for i,val in enumerate(prices):
            while stack and prices[stack[-1]]>=val:
                pricess[stack[-1]]=prices[stack[-1]]-val
                stack.pop()
                count+=1


            stack.append(i)
        return pricess

        