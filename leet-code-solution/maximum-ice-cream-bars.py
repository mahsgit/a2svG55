class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        mini=min(costs)
        maxi=max(costs)
        count_arr=[0]*(maxi-mini+1)
        res=[]
        for i in costs:
            count_arr[i-mini]+=1
        for i in range(len(count_arr)):
            res.extend([mini+i]*count_arr[i])
        count=0
        for j in res:
            if coins-j>=0:
                count+=1
                coins=coins-j
        return count
       


        