class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        new=[]
        result=defaultdict(int)
        num=""
        word=""
        final=[]
        for i in cpdomains:
            new=i.split()
            num=new[0]
            word=new[1].split('.')
            for j in range(len(word)):
                sub=".".join(word[j:])
                result[sub]+=int(num)
        for key,value in result.items():
            print(value,key)
            final.append(str(value)+' '+key)
        return final
            



        






            
           



        # print(dic)



            
             


           
           

           

        