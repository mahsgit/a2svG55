class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target=Counter(t)
        l=0
        ans=""
        mini=float('inf')
        if len(t)<=len(s):
            for r in range(len(s)):
                if s[r] in target:
                    target[s[r]]-=1
                    while max(target.values())<=0:
                        if r-l+1<mini:
                            ans=s[l:r+1]
                            mini=r-l+1
                        if s[l] in target:
                            target[s[l]]+=1
                        l+=1
        
            return ans
        else:
            return ""

       
                    
                


                
                
                
                


            
            
            
        