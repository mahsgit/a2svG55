class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
         check=Counter(s2[0:len(s1)])
         one=Counter(s1)
         if check==one:
             return True
         else:
            for i in range(len(s1),len(s2)):
                check[s2[i]]+=1
                check[s2[i-len(s1)]]-=1
                if check==one:
                    return True
            return False

      
            
           
            


        