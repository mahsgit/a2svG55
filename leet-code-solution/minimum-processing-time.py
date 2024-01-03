class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        t=len(tasks)
        p=len(processorTime)
        processorTime.sort(reverse=True)
        print(processorTime)
        print(tasks)

        ans=0
        a=0
        count=0
        for i in processorTime:
           for j in range(4):
               ans=max(ans,i+tasks[count])
               count+=1
         

            

     

        return ans
       
        