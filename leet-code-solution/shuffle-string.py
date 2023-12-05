class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:  
        st=""
        new_map=list(zip(s,indices))
        new_map.sort(key=lambda i: i[1])
        for i in new_map:
            st+=i[0]
        return st
        
