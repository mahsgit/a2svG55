class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        dp = {}
        def helper(l, r):
            if l == r:
                return nums[l]
            if (l, r) in dp:
                return dp[(l, r)]
            dp[(l, r)] = max(nums[l] - helper(l + 1, r), nums[r] - helper(l, r - 1))
            return dp[(l, r)]
        if helper(0, len(nums) - 1) < 0:
            return False
        return True


        

              
            
            
            
            