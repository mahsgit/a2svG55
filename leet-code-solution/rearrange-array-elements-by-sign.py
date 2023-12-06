class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negative =[]
        positive=[]
        out=[]
        for i in nums:
            if i<0:
                negative.append(i)
            elif i>0:
                positive.append(i)
        i=0
        while i <len(positive):
            out.append(positive[i])
            out.append(negative[i])
            i+=1
        return out


            

        