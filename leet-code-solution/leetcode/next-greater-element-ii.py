class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        l=len(nums)

        nums.extend(nums)
        stack=[]
        ans=['?']*l
        for i,val in enumerate(nums):
            while stack and nums[stack[-1]]<val:
                check=stack.pop()
                if check<l:
                    ans[check]=val
            stack.append(i)
        for i in range(len(ans)):
            if ans[i]=='?':
                ans[i]=-1


        return ans
        