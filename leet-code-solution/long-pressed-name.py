class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # i=0
        # j=0
        
        # while i<len(name) and j< len(typed):
        #     if name[i]==typed[j]:
        #         i+=1
        #         j+=1
        #     else:
        #         if typed[j]==typed[j-1] and j>0 :
        #             j+=1
        #         else:
        #             return False
        # if i==len(name) and j==len(typed):
        #     return True
        # if j<len(typed):
        #     while j<len(typed) and typed[j]==name[-1]:
        #         j+=1
        #     if j==len(typed):
        #         return True
        # if i<len(name):
        #     return False
           


        prev=None
        i=0
        for c in typed:
            if i<len(name) and c==name[i] :
                prev=c
                i+=1
            elif c==prev:
                continue
            else:
                return False
        return i==len(name)








       
      
        
      