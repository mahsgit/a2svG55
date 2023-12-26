class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        Map={}
        for h,name in zip(heights,names):
            Map[h]=name
        item=list(Map.keys())
        for i in range(len(Map)):
            for j in range(1,len(Map)-i):
                if item[j-1]<item[j]:
                    item[j-1],item[j]=item[j],item[j-1]
        ans=[]
        for i in item:
            ans.append(Map[i])
        return ans
        