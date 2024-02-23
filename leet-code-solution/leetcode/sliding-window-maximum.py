class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        new=deque()
        ans=[]
      
        for i in range(len(nums)):
            while new and nums[new[-1]]< nums[i]:
                new.pop()
            new.append(i)
            
            while new[-1]-new[0]>k-1:
                new.popleft()
            if i>=k-1:
              ans.append(nums[new[0]])
            
        return ans






    

              

        