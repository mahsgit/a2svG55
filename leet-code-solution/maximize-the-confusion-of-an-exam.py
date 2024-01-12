class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        tru='T'
        fal='F'
        tl=tf=0
        kl=kr=k
        maxil=0
        maxif=0
        length=len(answerKey)
        for t in range(length):
            if answerKey[t]=='F':
                kl-=1
                if kl<0:
                    while tl<length and answerKey[tl] !='F':
                        tl+=1
                    kl+=1
                    tl+=1                    
            maxil=max(maxil,t-tl+1)

       


        for f in range(length):
            if answerKey[f]=='T':
                kr-=1
                if kr<0:
                    while tf<length and answerKey[tf] !='T':
                        tf+=1
                    kr+=1
                    tf+=1 
            # print(maxif)                   
            maxif=max(maxif,f-tf+1)
       
        
        return max(maxil,maxif)

































        # tru='T'
        # fal='F'
        # l=0
        # maxit=0
        # maxif=0
        # kf=k

        # length=len(answerKey)
        # for i in range(length):
        #     if answerKey[i]!=tru:
        #         k-=1
        #         if k<0:
        #             remove=answerKey[i]
        #             while l<length and answerKey[l]!=remove:
        #                 l+=1
        #             # l+=1
        #             k+=1
        #     maxit=max(maxit,i-l+1)



        # fl=0   
        # for f in range(length):
        #     if answerKey[f]!=fal:
        #         kf-=1
        #         if kf<0:
        #             remove=answerKey[f]
        #             while fl<length and answerKey[fl]!=remove:
        #                 fl+=1
        #             # fl+=1
        #             kf+=1
        #     maxif=max(maxif,f-fl+1)
        #     print(maxif)
        # maxi=max(maxif,maxit)
        # return maxi


        