class Solution:
       def numberOfWays(self, s: str) -> int:
           possible=0
           one=zero=onezero=zeroone=0
           for val in s:
               if val=='0':
                   zero+=1
                   onezero+=one
                   possible+=zeroone
               else:
                    one+=1
                    zeroone+=zero
                    possible+=onezero
           return possible
        
        