class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix=[0]
        for i in range(len(nums)):
            self.prefix.append(self.prefix[-1]+nums[i])
        print(self.prefix)

        

    def sumRange(self, left: int, right: int) -> int:
        ans=self.prefix[right+1]-self.prefix[left]
        return ans
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)