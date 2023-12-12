class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total_even=0
        count=[]
        for i in nums:
            if i%2==0:
                total_even+=i
        for  val, ind in queries:
            if val % 2 ==0 and nums[ind]%2==0:

                total_even+=(nums[ind]+val) -nums[ind]
                nums[ind]+=val

            elif val % 2 !=0 and nums[ind]%2!=0:
                total_even+=val + nums[ind]
                nums[ind]+=val
            elif val % 2 !=0 and nums[ind]%2==0:
                total_even-= nums[ind]
                nums[ind]+=val
            else:
                nums[ind]+=val


            count.append(total_even)
        return count
            

            


        

        