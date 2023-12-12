class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        diction={}
       
        for i,value in  enumerate(nums):
            diction[value]=i



        for x, y in operations:
            nums[diction[x]]=y
            diction[y]=diction.pop(x)
          


               
        return nums
    
        