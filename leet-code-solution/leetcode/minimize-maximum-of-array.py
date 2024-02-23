class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        pref=[nums[0]]
        for val in nums[1:]:
            pref.append(pref[-1]+val)
        maxi=0
        for i, val in enumerate(pref):
            new=ceil(val/(i+1))

            maxi=max(maxi,new)

        return maxi