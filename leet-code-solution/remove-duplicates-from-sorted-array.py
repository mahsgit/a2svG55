class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
       i=0
       j=1
       count=1
       while j<len(nums):
           if nums[j]==nums[i]:
               j+=1
           else:
                nums[i+1]=nums[j]
                count+=1
                i+=1
       return count
                