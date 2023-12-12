class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        count=0
        for i in spaces:
            s = s[:i+count] + " " + s[i+count:]
            count+=1
        return s
        
        