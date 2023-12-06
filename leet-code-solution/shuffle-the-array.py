class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i=0
        j=n
        out=[]
        while j<len(nums):
            out.append(nums[i])
            out.append(nums[j])
            j+=1
            i+=1
        return out

