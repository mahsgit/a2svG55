class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        mapp=defaultdict()
        first=[]

        for i,val in enumerate(intervals):
            mapp[val[0]]=i
            first.append(val[0])
        first.sort()
        leng=len(first)-1
        def checker(la):
            l=0
            r=leng
            temp=-1
            while l<=r:
                mid=(l+r)//2
                if first[mid]>=la:
                    temp = mapp[first[mid]]
                    r=mid-1
                else:
                    l=mid+1
            return temp
            

        ans=[]
        for f,la in intervals:
           ans.append(checker(la))
    
        return ans
    

        