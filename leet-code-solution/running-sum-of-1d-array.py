class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # ans=[]
        # val=0
        # for i  in range(len(nums)):
        #     val+=nums[i]
        #     ans.append(val)
        # return ans


        # sum_arr = [nums[0]]
        # for i in range(1, len(nums)):
        #     sum_arr.append(nums[i] + sum_arr[-1])
            
        # return sum_arr

        #   for i in range(1, len(nums)):
        #     nums[i] += nums[i-1]

        #   return nums
          ans=[nums[0]]


          for i in range(1,len(nums)):
              ans.extend([ans[-1]+nums[i]])
          return ans

          
