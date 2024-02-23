class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        new=deque(range(len(tickets)))
        ans=0
        while tickets[k]>0:
            tickets[new[0]]-=1
            ind=new.popleft()
            ans+=1
            if tickets[ind]>0:
                new.append(ind)
        

        return ans
            
        