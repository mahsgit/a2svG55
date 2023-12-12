class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
       
       Map={}
       mini=float("inf")

       for i in range(len(list1)):
           Map[list1[i]]=i
       for j in range(len(list2)):
           if list2[j] in Map:
               print(list2[j])
               total=j+Map[list2[j]]
               if total<mini:
                   mini=total
                   res=[]
                   res.append(list2[j])
               elif total==mini:
                   res.append(list2[j])


                   
       return res



            
            