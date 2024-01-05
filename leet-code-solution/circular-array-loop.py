class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        l=len(nums)
        visited=set()
        for i in range(len(nums)):
            count=0
            ptr=(nums[i]+i)%l
            if nums[i]>0 :
                while (i!=ptr and nums[ptr]>0 ):
                    ptr=(nums[ptr]+ptr)%l
                    count+=1
                    if count>l:
                        break

                if i==ptr and count>0:
                    return True

            else:
                while i!=ptr and nums[ptr]<0:
                    ptr=(nums[ptr]+ptr)%l
                    count+=1
                    if count>l:
                        break
                
                if i==ptr and count>0 :
                    return True
           
        return False







            