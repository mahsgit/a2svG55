class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        up=0
        down=0
        n=len(firstList)
        m=len(secondList)
        ans=[]

        while up<n and down <m:
            lu,ru=firstList[up]
            ld,rd=secondList[down]


            left=max(lu,ld)
            right=min(ru,rd)

            if left<=right:
                ans.append([left,right])

            if ru>=rd:
                down+=1
            else:
                up+=1
        return ans 
