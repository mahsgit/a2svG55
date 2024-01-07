class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        summ = sum(nums[:k])
        average = summ / k

        for i in range(k, len(nums)):
            summ += nums[i] - nums[i - k]
            average = max(average,summ / k)

        return average