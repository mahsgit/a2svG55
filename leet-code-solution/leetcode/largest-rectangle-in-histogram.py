class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxi=0
        leng=len(heights)
        for i ,val in enumerate(heights):
            temp=i
            while stack and stack[-1][1]>val:
                j,n=stack.pop()
                maxi=max(maxi,n*(i-j))
                temp=j

            
            stack.append((temp,val))
        for j,n in stack:
                maxi=max(maxi,n*(leng-j))

        return maxi
        