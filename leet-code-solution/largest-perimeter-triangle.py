class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        j=ans=0
        nums.sort(reverse=True)
        print(nums)
      
        for j in range(len(nums)-2):
            if nums[j]<nums[j+1]+nums[j+2]:
                return sum(nums[j:j+3])
            
          
        return 0
      
        
       

        