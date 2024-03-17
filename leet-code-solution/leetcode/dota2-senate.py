class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queR=deque()
        queD=deque()
        ans=""
        leng=len(senate)
        for i,s in enumerate(senate):
            if s=="R":
                queR.append(i)
            else:
                queD.append(i)
        while queR and queD:
            di=queD.popleft()
            ra=queR.popleft()
            if di<ra:
                queD.append(di+leng)
            else:
                queR.append(ra+leng)
        if queR:
            return "Radiant"
        else:
            return "Dire"
      
        