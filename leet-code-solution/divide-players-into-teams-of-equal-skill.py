class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i=0
        j=len(skill)-1
        new=0
        while i<=j:
            if skill[i]+skill[j]==skill[i+1]+skill[j-1]:
                new+=skill[i]*skill[j]
                i+=1
                j-=1
            else:
                return -1
        return new


        