class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        new=[0]*len(s)
        for l,r,v in shifts:
            if v==0:
                new[l]-=1
                if r!=len(s)-1:
                  new[r+1]+=1
            elif v==1:
                new[l]+=1
                if r!=len(s)-1:
                  new[r+1]-=1
        pre=[new[0]]

        for i in range(1,len(new)):
            pre.append(pre[-1]+new[i])
        ans=""
        for st,num in zip(s,pre):
            check= chr((((ord(st)-97)+num)%26)+97)
            ans+=check
           
        return ans
        
        

         



            
        