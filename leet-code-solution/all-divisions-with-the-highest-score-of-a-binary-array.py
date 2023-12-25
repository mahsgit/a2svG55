class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
    
        # length=len(nums)
        # best=score=sum(nums)
        # ans=[0]
        # for l in range(length):
        #     if nums[l]==0:
        #         score+=1
        #     else:
        #         score-=1
            
        #     if best==score:
        #         ans.append(l+1)
                
        #     elif best<score:
        #         best=score
        #         ans=[l+1]
        # return ans
        # zero=[]
        # one=[]
        # for i in nums:
        #     if nums[i]=0:

        zero=a=0
        Map=defaultdict(int)
        one=sum(nums)
        new=[]
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                Map[i]=zero+one
                zero+=1
            else:
                Map[i]=zero+one
                one-=1

        Map[n]=zero
        big=max(Map.values())
        for key , value in Map.items():
            if value==big:
                new.append(key)
          
        return new


                

