class Solution:
    def smallestNumber(self, num: int) -> int:
        if num>0:
            num=str(num)
            num=list(map(int,num))
            num.sort()
            i=0
            j=1
            if num[i]==0:
                while num[j]==0:
                    j+=1
                num[0],num[j]=num[j],num[0]


            ans="".join(map(str,num))
            return int(ans)

        elif num<0:
            num=str(num)
            num=num[1:]
            num=list(map(int,num))
            num.sort(reverse=True )

            ans="".join(map(str,num))
            return -int( ans)
        else:
            return 0





        
