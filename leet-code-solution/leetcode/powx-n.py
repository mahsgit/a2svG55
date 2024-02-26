class Solution:
    def myPow(self, x: float, n: int) -> float:
            @cache
            def powaa(n):
                if n==0:
                    return 1
                elif n==1:
                    return x
                num=powaa(n-n//2)*powaa(n//2)
                return num
                #   return num*=x
        
            
            # if n==0 :
            #     return 1
            # elif  x==0:
            #     return 0
            if n>=0:
                return powaa(abs(n))
            else:
               return 1/powaa(abs(n))
     
