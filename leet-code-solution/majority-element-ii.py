class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res=[]
        N=len(nums)
        c=Counter(nums)
        print(c)
        print(c.items)

        return[i for i,n in c.items() if n>(N//3)]