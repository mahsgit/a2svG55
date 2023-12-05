class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        out=[]
        for i in range(1,len(nums),2):
            n=nums[i-1]
            for j in range(n):
                out.append(nums[i])
        return out


        