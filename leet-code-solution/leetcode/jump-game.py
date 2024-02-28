class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr=0
        for val in nums:
            if curr<0:
                return False
            else:
                if curr<val:
                    curr=val
            curr-=1
        return True

      