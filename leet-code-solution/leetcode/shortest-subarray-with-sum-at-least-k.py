class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        que=deque()
        pref=[[0,0]]
        for i,val in enumerate(nums):
            pref.append([i+1,pref[-1][1]+val])

        que=deque()
        mini=float('inf')
        print(pref)

        for i,v in pref:
            while que and que[-1][1]>=v:
                j,n=que.pop()
                while que and n-que[0][1]>=k:
                    mini=min(mini,j-que[0][0])
                    que.popleft()


            que.append((i,v))
           
            while que and que[-1][1]-que[0][1]>=k:
                mini=min(mini,que[-1][0]-que[0][0])
                que.popleft()

       

        if mini==float('inf'):
            return -1
        else:
            return mini

       
        