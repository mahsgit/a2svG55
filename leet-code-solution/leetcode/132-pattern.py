class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # stack=[]
        # mini=nums[0]
        # for val in nums[1:]:
        #     while stack and val>=stack[-1][0]:
        #         stack.pop()
        #     if stack and  val > stack[-1][1]:
        #         return True
        #     stack.append([val,mini])
        #     mini=min(mini,val)
        # return False
        stack, k = [], -float('inf')

        for n in reversed(nums):
            if n < k:
                return True
            while stack and stack[-1] < n:
                k = stack.pop()
            stack.append(n)
        return False 


        