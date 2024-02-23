class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[-1]*len(nums1)
        stack=[]
        mapp=defaultdict(lambda:-1)
        for i,val in enumerate(nums1):
            mapp[val]=i
        for val in nums2:
            while stack  and val > stack[-1] :
                n=stack.pop()
                if mapp[n]>=0:
                  ans[mapp[n]]=val

            stack.append(val)
        return ans
        